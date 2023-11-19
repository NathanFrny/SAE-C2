from __future__ import annotations
from .GradientStrategy import GradientStrategy

class GradientSelector:

    def __init__(self: GradientSelector):
        self._method: GradientStrategy = None

    @property
    def method(self: GradientSelector) -> GradientStrategy:
        return self._method
    @method.setter
    def method(self: GradientSelector, method: GradientStrategy):
        self._method = method
    
    def execute(self: GradientSelector):
        self._method.generate()