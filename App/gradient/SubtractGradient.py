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
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Class
class SubtractGradient(GradientStrategy):
    """
    A class representing a simple gradient subtraction strategy. It subtracts a given gradient from the image.

    Attributes:
        img (np.ndarray): The original image.
        gradient_path (str): The path to the gradient image.

    Methods:
        generate(self: SubtractGradient) -> np.ndarray:
            Generate an image by subtracting the gradient from the original image.

    """
    def __init__(self: GradientStrategy, path, gradient_path):
        """
        Initializes a SubtractGradient object.

        Parameters:
            path (str): The path to the original image.
            gradient_path (str): The path to the gradient image.

        """
        self.img = cv2.imread(path)
        self.gradient_path = gradient_path

    def generate(self: GradientStrategy):
        """
        Generate an image by subtracting the gradient from the original image.

        Returns:
            np.ndarray: The resulting image after gradient subtraction.

        """
        print(self.gradient_path)
        gradient = cv2.imread(self.gradient_path)
        result = cv2.subtract(self.img, gradient)
        result = cv2.subtract(result, gradient)
        return result
# ----------------------------------------------------------------------------------------------------------------------
