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
class Saturation(ImageDecorator):
    """
    Class representing a saturation image decorator.

    Attributes:
        factor (float): The factor by which to adjust the saturation.

    Methods:
        apply(self: Saturation, image):
            Applies a saturation modification to the given image.

    """
    def __init__(self: Saturation, factor: float):
        """
        Initializes a Saturation instance.

        Parameters:
            factor (float): The factor by which to adjust the saturation.

        """
        self.factor = factor

    def apply(self, image):
        """
        Applies a saturation modification to the given image.

        Parameters:
            image: The image to which the saturation modification is applied.

        Returns:
            numpy.ndarray: The modified image.

        """
        print("Saturation")
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
        h, s, v = cv2.split(hsv)
        
        # Ajuster la saturation
        s = np.clip(s * self.factor, 0, 255)
        
        # Fusionner les canaux HSV ajustés
        hsv_modified = cv2.merge([h, s, v])
        
        # Convertir l'image modifiée de HSV à BGR
        return cv2.cvtColor(hsv_modified.astype(np.uint8), cv2.COLOR_HSV2BGR)
# ----------------------------------------------------------------------------------------------------------------------
