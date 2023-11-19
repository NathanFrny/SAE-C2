from __future__ import annotations
from .ImageDecorator import ImageDecorator
import numpy as np
import cv2


class Gamma(ImageDecorator):
    """
    A class representing the Gamma decorator for image processing.

    Attributes:
        gamma (float): The gamma parameter for the gamma correction.

    Methods:
        __init__(self, gamma: float): Initializes the Gamma decorator with the given gamma value.

        apply(self, image): Applies the gamma correction to the input image.

    """
    def __init__(self: Gamma, gamma: float):
        """
        Initializes the Gamma decorator with the given gamma value.

        Args:
            gamma (float): The gamma parameter for the gamma correction.

        """
        self.gamma = gamma

    def apply(self, image):
        """
        Initializes the Gamma decorator with the given gamma value.

        Args:
            gamma (float): The gamma parameter for the gamma correction.

        """
        print("Gamma")
        # Séparer les canaux de couleur
        blue, green, red = cv2.split(image)

        # Appliquer la correction gamma à chaque canal séparément
        gamma_table = np.array([((i / 255.0) ** self.gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

        red_corrected = cv2.LUT(red, gamma_table)
        green_corrected = cv2.LUT(green, gamma_table)
        blue_corrected = cv2.LUT(blue, gamma_table)

        # Fusionner les canaux corrigés
        corrected_image = cv2.merge((blue_corrected, green_corrected, red_corrected))

        return corrected_image
        
