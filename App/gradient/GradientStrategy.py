from __future__ import annotations
from abc import ABC, abstractmethod

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