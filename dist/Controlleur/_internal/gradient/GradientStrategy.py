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
class GradientStrategy(ABC):
    """
    Abstract base class for gradient strategies.

    Methods:
        generate(self: GradientStrategy):
            Abstract method to generate a gradient.

    """
    @abstractmethod
    def generate(self: GradientStrategy):
        """
        Abstract method to generate a gradient.

        """
        pass
# ----------------------------------------------------------------------------------------------------------------------
