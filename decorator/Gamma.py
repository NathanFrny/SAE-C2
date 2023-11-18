from __future__ import annotations
from ImageDecorator import ImageDecorator
import numpy as np
import cv2


class Gamma(ImageDecorator):
    def __init__(self: Gamma, gamma: float):
        self.gamma = gamma

    def apply(self, image):
        gamma_table = np.array([((i / 255.0) ** self.gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(image, gamma_table)
        
