from __future__ import annotations
from .GradientStrategy import GradientStrategy
from PyQt6.QtWidgets import QFileDialog
import cv2

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