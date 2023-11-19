from __future__ import annotations
from abc import ABC, abstractmethod

class ImageDecorator(ABC):
    """
    Abstract interface for images decorators.
    """
    @abstractmethod
    def apply(self: ImageDecorator):
        """
        functions that apply a modification on a image

        parameter:
            factor (int): The modification to apply of any factor of an images
        """
        pass
