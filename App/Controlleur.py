import sys
import Vue_Traitement
import SliderWidget
import Traitement
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
            self.update_image(self.vue.gamma_widget.value)

    def on_saturation_changed(self):
        if self.vue.saturation_checkbox.isChecked():
            self.update_image(self.vue.saturation_widget.value)

    def on_blur_changed(self):
        if self.vue.blur_checkbox.isChecked():
            self.update_image(self.vue.blur_widget.value)

    def update_image(self, value):
        print(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlleur = Controlleur()
    controlleur.vue.show()
    app.exec()
        