from __future__ import annotations
from .ImageDecorator import ImageDecorator
import numpy as np
import cv2


class Saturation(ImageDecorator):
    def __init__(self: Saturation, factor: float):
        self.factor = factor

    def apply(self, image):
        print("Saturation")
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
        h, s, v = cv2.split(hsv)
        
        # Ajuster la saturation
        s = np.clip(s * self.factor, 0, 255)
        
        # Fusionner les canaux HSV ajustés
        hsv_modified = cv2.merge([h, s, v])
        
        # Convertir l'image modifiée de HSV à BGR
        return cv2.cvtColor(hsv_modified.astype(np.uint8), cv2.COLOR_HSV2BGR)
