from __future__ import annotations
from .GradientStrategy import GradientStrategy

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