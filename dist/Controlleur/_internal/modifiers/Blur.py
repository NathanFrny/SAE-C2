from __future__ import annotations
from .ImageDecorator import ImageDecorator
import cv2

class Blur(ImageDecorator):
    """
    A class representing the Blur decorator for image processing.

    Attributes:
        radius (float): The radius parameter for the blur effect.

    Methods:
        __init__(self, radius: float): Initializes the Blur decorator with the given radius.

        apply(self, image): Applies the blur effect to the input image.

    """
    def __init__(self: Blur, radius: float):
        """
        Initializes the Blur decorator with the given radius.

        Args:
            radius (float): The radius parameter for the blur effect.

        """
        self.radius = radius

    def apply(self, image):
        """
        Applies the blur effect to the input image.

        Args:
            image: The input image.

        Returns:
            Image: The image after applying the blur effect.

        """
        print("Blur")
        if self.radius % 2 == 1:
            return cv2.GaussianBlur(image, (self.radius, self.radius), 0)
        return image

    