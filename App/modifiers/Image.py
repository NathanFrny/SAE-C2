from __future__ import annotations
from .ImageDecorator import ImageDecorator
import cv2

class Image(ImageDecorator):
    """ Class that represent an image.
    """
    def __init__(self: Image, path: str | Image, decorators: ImageDecorator = []):
        if (isinstance(path, str)):
            self.image = cv2.imread(path)
        else:
            self.image = path
        self.decorators: list[ImageDecorator] = decorators

    def apply(self, image):
        updated_image = self.image
        for decorator in self.decorators:
            updated_image = decorator.apply(updated_image)
        self.image = updated_image

    def add_decorator(self: Image, decorator: ImageDecorator):
        print(self.decorators)
        if decorator not in self.decorators:
            new_decorator = self.decorators + [decorator]
        return Image(self.image, new_decorator)

    def remove_decorator(self, decorator_type: ImageDecorator):
        for decorator in self.decorators:
            if isinstance(decorator, decorator_type):
                self.decorators.remove(decorator)