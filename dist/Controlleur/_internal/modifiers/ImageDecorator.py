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
from abc import ABC, abstractmethod
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Class
class ImageDecorator(ABC):
    """
    Abstract interface for image decorators.

    Methods:
        apply(self: ImageDecorator):
            Applies a modification to an image.

    """
    @abstractmethod
    def apply(self: ImageDecorator):
        """
        functions that apply a modification on a image

        parameter:
            factor (int): The modification to apply of any factor of an images
        """
        pass
# ----------------------------------------------------------------------------------------------------------------------

