from __future__ import annotations
from ImageDecorator import ImageDecorator
import cv2

class Image(ImageDecorator):
    """ Class that represent an image.
    """
    def __init__(self: Image, path: str):
        self.image = cv2.imread(path)

    def apply(self, processor):
        self.image = processor.apply(self.image)