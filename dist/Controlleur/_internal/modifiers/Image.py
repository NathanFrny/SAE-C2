from __future__ import annotations
from .ImageDecorator import ImageDecorator
import cv2

class Image(ImageDecorator):
    """
    Class representing an image with the ability to apply decorators for image processing.

    Attributes:
        image: The underlying image data.
        decorators (list): A list of ImageDecorator instances to be applied to the image.

    Methods:
        __init__(self, path: str | Image, decorators: list[ImageDecorator] = []): Initializes the Image with the given path or image and optional decorators.

        apply(self, image): Applies the decorators to the image.

        add_decorator(self, decorator: ImageDecorator): Adds a new decorator to the image.

        remove_decorator(self, decorator_type: ImageDecorator): Removes a decorator of the specified type from the image.

    """
    def __init__(self: Image, path: str | Image, decorators: ImageDecorator = []):
        """
        Initializes the Image with the given path or image and optional decorators.

        Args:
            path (str | Image): The path to the image file or an existing image.
            decorators (list[ImageDecorator]): Optional list of ImageDecorator instances.

        """
        if (isinstance(path, str)):
            self.image = cv2.imread(path)
        else:
            self.image = path
        self.decorators: list[ImageDecorator] = decorators

    def apply(self, image):
        """
        Applies the decorators to the image.

        Args:
            image: The input image.

        Returns:
            None

        """
        updated_image = self.image
        for decorator in self.decorators:
            updated_image = decorator.apply(updated_image)
        self.image = updated_image

    def add_decorator(self: Image, decorator: ImageDecorator):
        """
        Adds a new decorator to the image.

        Args:
            decorator (ImageDecorator): The decorator to be added.

        Returns:
            Image: A new Image instance with the added decorator.

        """
        print(self.decorators)
        if decorator not in self.decorators:
            new_decorator = self.decorators + [decorator]
        return Image(self.image, new_decorator)

    def remove_decorator(self, decorator_type: ImageDecorator):
        """
        Removes a decorator of the specified type from the image.

        Args:
            decorator_type (ImageDecorator): The type of decorator to be removed.

        Returns:
            None

        """
        for decorator in self.decorators:
            if isinstance(decorator, decorator_type):
                self.decorators.remove(decorator)