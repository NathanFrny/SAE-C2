from __future__ import annotations
from .GradientStrategy import GradientStrategy
from PyQt6.QtWidgets import QFileDialog
import cv2

class SubtractGradient(GradientStrategy):

    def __init__(self: GradientStrategy, path, gradient_path):
        self.img = cv2.imread(path)
        self.gradient_path = gradient_path

    def generate(self: GradientStrategy):
        print(self.gradient_path)
        gradient = cv2.imread(self.gradient_path)
        result = cv2.subtract(self.img, gradient)
        result = cv2.subtract(result, gradient)
        return result