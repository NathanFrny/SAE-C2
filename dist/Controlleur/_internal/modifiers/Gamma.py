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
from .ImageDecorator import ImageDecorator
import numpy as np
import cv2
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Class
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
# ----------------------------------------------------------------------------------------------------------------------

        
