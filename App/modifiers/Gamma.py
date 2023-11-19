from __future__ import annotations
from .ImageDecorator import ImageDecorator
import numpy as np
import cv2


class Gamma(ImageDecorator):
    def __init__(self: Gamma, gamma: float):
        self.gamma = gamma

    def apply(self, image):
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
        
