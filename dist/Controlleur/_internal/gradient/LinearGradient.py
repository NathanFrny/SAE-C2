# ----------------------------------------------------------------------------------------------------------------------
#
# Authors : Fourny Nathan
# Copyright (C) 2023 Fourny Nathan
# 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Imports
from __future__ import annotations
from .GradientStrategy import GradientStrategy
import cv2
import numpy as np
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Class
class LinearGradient(GradientStrategy):
    """
    A class representing a linear gradient subtraction strategy. It create a gradient by interpolating between four points on the image. Then it subtracts the gradient from the image.

    Attributes:
        path (str): The path to the image.

    Methods:
        generate(self: LinearGradient) -> np.ndarray:
            Generate a depolluted image using linear gradient subtraction.

    """
    def __init__(self: LinearGradient, path):
        """
        Initializes a LinearGradient object.

        Parameters:
            path (str): The path to the image.

        """
        self.path = path

    def generate(self: LinearGradient):
        """
        Generate a depolluted image using linear gradient subtraction.

        Returns:
            np.ndarray: The depolluted image.

        """
        image = cv2.imread(self.path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if image_gray is None or self.path is None:
            print("Failed to load one or more images.")
        else:

            height, width, _ = image.shape
            if height > 2000 or width > 2000:
                num_columns_to_check = 1
            else:
                num_columns_to_check = 3

            threshold_value = 128

            depolluted_image, gradient_linear = self.remove_light_pollution(image, image_gray, num_columns_to_check, threshold_value)

            return depolluted_image

    def remove_light_pollution(self: LinearGradient, image_color, image_gray, num_columns, threshold):
        """
        Remove light pollution from the image using linear gradient subtraction.

        Parameters:
            image_color (np.ndarray): The color image.
            image_gray (np.ndarray): The grayscale image.
            num_columns (int): The number of columns to check for light pollution.
            threshold (int): The threshold value.

        Returns:
            tuple[np.ndarray, np.ndarray]: The depolluted image and the linear gradient.

        """
        height, width, _ = image_color.shape

        # Find the point without stars on the left side of the grayscale image
        for x in range(num_columns):
            for y in range(height):
                if np.any(image_gray[y, x] <= threshold):
                    left_x = x
                    break
            if left_x is not None:
                break

        # Find the point without stars at the 1/3 of the grayscale image
        one_third_x = width // 3
        for y in range(height):
            if np.any(image_gray[y, one_third_x] <= threshold):
                break

        # Find the point without stars at the 2/3 of the grayscale image
        two_thirds_x = 2 * (width // 3)
        for y in range(height):
            if np.any(image_gray[y, two_thirds_x] <= threshold):
                break

        # Find the point without stars on the right side of the grayscale image
        for x in range(width - 1, width - num_columns - 1, -1):
            for y in range(height):
                if np.any(image_gray[y, x] <= threshold):
                    right_x = x
                    break
            if right_x is not None:
                break

        if left_x is not None and right_x is not None:
            # Get the colors of the left, 1/3, 2/3, and right pixels in the color image
            color_pixel_left = image_color[0, left_x]
            color_pixel_one_third = image_color[0, one_third_x]
            color_pixel_two_thirds = image_color[0, two_thirds_x]
            color_pixel_right = image_color[0, right_x]

            # Generate a horizontal linear gradient using the four color points
            gradient_linear = np.zeros((height, width, 3), dtype=np.uint8)

            for x in range(width):
                for y in range(height):
                    if x <= one_third_x:
                        ratio = (x - left_x) / (one_third_x - left_x)
                        interpolated_color = (1 - ratio) * color_pixel_left + ratio * color_pixel_one_third
                    elif x <= two_thirds_x:
                        ratio = (x - one_third_x) / (two_thirds_x - one_third_x)
                        interpolated_color = (1 - ratio) * color_pixel_one_third + ratio * color_pixel_two_thirds
                    else:
                        ratio = (x - two_thirds_x) / (right_x - two_thirds_x)
                        interpolated_color = (1 - ratio) * color_pixel_two_thirds + ratio * color_pixel_right
                    gradient_linear[y, x] = interpolated_color

            # Subtract the linear gradient from the color image
            image_depolluted = cv2.subtract(image_color, gradient_linear)

            return image_depolluted, gradient_linear # Return the depolluted image with the gradient linear
        else:
            print("No point without stars found.")
            return image_color  # Return the original image 
# ----------------------------------------------------------------------------------------------------------------------
