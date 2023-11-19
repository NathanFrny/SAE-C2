from __future__ import annotations
from abc import ABC, abstractmethod

class GradientStrategy(ABC):
    @abstractmethod
    def generate(self: GradientStrategy): pass