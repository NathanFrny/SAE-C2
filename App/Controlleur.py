# ----------------------------------------------------------------------------------------------------------------------
#
# Authors : Bonnel Noah
# Copyright (C) 2023 Bonnel Noah
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

import sys
import Vue_Traitement
from modifiers import Blur, Saturation, Gamma
from PyQt6.QtWidgets import QApplication
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Class
class Controlleur:
    """
        This class serves as the controller for the image processing application.

        Attributes:
            traitement (Traitement.Traitement): An instance of the Traitement class for image processing.
            vue (Vue_Traitement.Vue_Traitement): An instance of the Vue_Traitement class for the user interface.

        Methods:
            __init__(self): Initializes the controller by creating instances of Traitement and Vue_Traitement.
            on_gamma_changed(self): Method called when the gamma slider value changes.
            on_saturation_changed(self):  Method called when the saturation slider value changes.
            on_blur_changed(self):  Method called when the blur slider value changes.
            update_image(self, decorator): Updates the displayed image with the given decorator.
    """
    def __init__(self):
        """
        Initializes the Controlleur class.

        Creates instances of Vue_Traitement.
        Connects the signals from the Vue_Traitement to the corresponding methods in the controller.
        """
        
        self.vue = Vue_Traitement.Vue_Traitement()

        # Connect signals from the Vue_Traitement to controller slots
        self.vue.gamma_widget.valueChanged.connect(self.on_gamma_changed)
        self.vue.saturation_widget.valueChanged.connect(self.on_saturation_changed)
        self.vue.blur_widget.valueChanged.connect(self.on_blur_changed)

    def on_gamma_changed(self):
        """
        Method called when the gamma slider value changes.

        If the gamma checkbox is checked and there is a local image, applies the gamma decorator to the image.
        Updates the displayed image.
        """
        if self.vue.gamma_checkbox.isChecked():
            if self.vue.local_image:
                self.vue.local_image.remove_decorator(Gamma)
                self.vue.gamma_decorator = Gamma(self.vue.gamma_widget.value)
                self.vue.local_image = self.vue.local_image.add_decorator(self.vue.gamma_decorator)
                self.update_image(self.vue.gamma_decorator)

    def on_saturation_changed(self):
        """
        Method called when the saturation slider value changes.

        If the saturation checkbox is checked and there is a local image, applies the saturation decorator to the image.
        Updates the displayed image.
        """
        if self.vue.saturation_checkbox.isChecked():
            if self.vue.local_image:
                self.vue.local_image.remove_decorator(Saturation)
                self.vue.saturation_decorator = Saturation(self.vue.saturation_widget.value)
                self.vue.local_image = self.vue.local_image.add_decorator(self.vue.saturation_decorator)
                self.update_image(self.vue.saturation_decorator)

    def on_blur_changed(self):
        """
        Method called when the saturation slider value changes.

        If the saturation checkbox is checked and there is a local image, applies the saturation decorator to the image.
        Updates the displayed image.
        """
        if self.vue.blur_checkbox.isChecked():
            if self.vue.local_image:
                self.vue.local_image.remove_decorator(Blur)
                self.vue.blur_decorator = Blur(self.vue.blur_widget.value)
                self.vue.local_image = self.vue.local_image.add_decorator(self.vue.blur_decorator)
                self.update_image(self.vue.blur_decorator)

    def update_image(self, decorator):
        """
        Updates the displayed image with the given decorator.

        Args:
            decorator: The image decorator to be applied.
        """
        self.vue.update_image(decorator)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlleur = Controlleur()
    controlleur.vue.show()
    app.exec()

# ----------------------------------------------------------------------------------------------------------------------

        