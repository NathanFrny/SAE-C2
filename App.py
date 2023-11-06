import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
import cv2

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #initialisation interface
        self.setWindowTitle("Traitement d'Images Astronomiques")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.load_image_button = QPushButton("Charger Image")
        self.load_image_button.clicked.connect(self.load_image)
        layout.addWidget(self.load_image_button)

        self.load_gradient_button = QPushButton("Charger Gradient")
        self.load_gradient_button.clicked.connect(self.load_gradient)
        layout.addWidget(self.load_gradient_button)

        self.process_button = QPushButton("Soustraire le Gradient")
        self.process_button.clicked.connect(self.subtract_gradient)
        layout.addWidget(self.process_button)
        
        self.display_button = QPushButton("Afficher l'image")
        self.display_button.clicked.connect(self.display_image)
        layout.addWidget(self.display_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.central_widget.setLayout(layout)

    def load_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.jpg *.png)")
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            self.image = cv2.imread(selected_file)
            self.result_label.setText("Image chargée")

    def load_gradient(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.jpg *.png)")
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            self.gradient = cv2.imread(selected_file)
            self.result_label.setText("Gradient chargé")

    def subtract_gradient(self):
        if hasattr(self, 'image') and hasattr(self, 'gradient'):
            result = cv2.subtract(self.image, self.gradient)
            result = cv2.subtract(result, self.gradient)
            result = cv2.subtract(result, self.gradient)
            result = cv2.subtract(result, self.gradient)
            cv2.imwrite('images/result.jpg', result)
            self.result_label.setText("Soustraction terminée. Résultat sauvegardé sous 'result.jpg'")
        else:
            self.result_label.setText("Veuillez charger l'image et le gradient d'abord.")
            
    def display_image(self):
        if hasattr(self, 'image'):
            resultat = cv2.imread('images/result.jpg')
            cv2.imshow("Image", resultat)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            self.result_label.setText("Veuillez d'abord soustraire un gradient")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
