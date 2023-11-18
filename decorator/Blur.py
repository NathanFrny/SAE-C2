from __future__ import annotations
from ImageDecorator import ImageDecorator
import cv2

class Blur(ImageDecorator):
    def __init__(self: Blur, radius: float):
        self.radius = radius

    def apply(self, image):
        return cv2.GaussianBlur(image, (self.radius, self.radius), 0)

    