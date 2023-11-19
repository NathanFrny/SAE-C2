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
from .GradientStrategy import GradientStrategy
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Class
class GradientSelector:
    """
    Class for selecting and executing gradient methods.

    Attributes:
        _method (GradientStrategy): The selected gradient method.

    Properties:
        method (GradientStrategy): Get or set the current gradient method.

    Methods:
        execute(self: GradientSelector):
            Execute the selected gradient method.

    """
    def __init__(self: GradientSelector):
        """
        Initializes a GradientSelector instance.

        """
        self._method: GradientStrategy = None

    @property
    def method(self: GradientSelector) -> GradientStrategy:
        """
        Get the current gradient method.

        Returns:
            GradientStrategy: The current gradient method.

        """
        return self._method
    @method.setter
    def method(self: GradientSelector, method: GradientStrategy):
        """
        Set the current gradient method.

        Parameters:
            method (GradientStrategy): The gradient method to set.

        """
        self._method = method
    
    def execute(self: GradientSelector):
        """
        Execute the selected gradient method.

        """
        self._method.generate()
# ----------------------------------------------------------------------------------------------------------------------
