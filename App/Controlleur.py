import sys
import Vue_Traitement
import SliderWidget
import Traitement
from modifiers import Blur, Saturation, Gamma, Image
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, pyqtSignal

class Controlleur:

    def __init__(self):
        self.traitement = Traitement.Traitement()
        self.vue = Vue_Traitement.Vue_Traitement()

        # Connecter les signaux de la vue aux slots du contrôleur
        self.vue.gamma_widget.valueChanged.connect(self.on_gamma_changed)
        self.vue.saturation_widget.valueChanged.connect(self.on_saturation_changed)
        self.vue.blur_widget.valueChanged.connect(self.on_blur_changed)

    # Les slots qui seront appelés lorsque les valeurs des sliders changent
    def on_gamma_changed(self):
        if self.vue.gamma_checkbox.isChecked():
            if self.vue.local_image:
                self.vue.local_image.remove_decorator(Gamma)
                self.vue.gamma_decorator = Gamma(self.vue.gamma_widget.value)
                self.vue.local_image = self.vue.local_image.add_decorator(self.vue.gamma_decorator)
                self.update_image(self.vue.gamma_decorator)

    def on_saturation_changed(self):
        if self.vue.saturation_checkbox.isChecked():
            if self.vue.local_image:
                self.vue.local_image.remove_decorator(Saturation)
                self.vue.saturation_decorator = Saturation(self.vue.saturation_widget.value)
                self.vue.local_image = self.vue.local_image.add_decorator(self.vue.saturation_decorator)
                self.update_image(self.vue.saturation_decorator)

    def on_blur_changed(self):
        if self.vue.blur_checkbox.isChecked():
            if self.vue.local_image:
                self.vue.local_image.remove_decorator(Blur)
                self.vue.blur_decorator = Blur(self.vue.blur_widget.value)
                self.vue.local_image = self.vue.local_image.add_decorator(self.vue.blur_decorator)
                self.update_image(self.vue.blur_decorator)

    def update_image(self, decorator):
        self.vue.update_image(decorator)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlleur = Controlleur()
    controlleur.vue.show()
    app.exec()
        