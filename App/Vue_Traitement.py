from __future__ import annotations
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QComboBox, QSlider, QSpacerItem, QSizePolicy, QCheckBox, QLineEdit
from PyQt6.QtGui import QPixmap, QImage, QIntValidator
from PyQt6.QtCore import Qt, pyqtSignal
import cv2
from ImageWidget import ImageWidget
from SliderWidget import SliderWidget

#class vue affichage interface traitement d'image
class Vue_Traitement(QWidget):
    
    gammaValue : pyqtSignal = pyqtSignal(int)
    saturationValue : pyqtSignal = pyqtSignal(int)
    blurValue : pyqtSignal = pyqtSignal(int)


    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traitement d'images")
        self.setFixedSize(1000, 500)
        
        self.mainlayout = QHBoxLayout()
        
        # left side of the window
        self.left = QWidget()
        self.leftlayout = QVBoxLayout()
        self.left.setLayout(self.leftlayout)
        
        # right side of the window
        self.right = QWidget()
        self.rightlayout = QVBoxLayout()
        self.right.setLayout(self.rightlayout)
        
        # Spacer Init to make space between widgets
        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # left side of the window
        
        # QComboBox used to select the method
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Choisir une méthode")
        self.comboBox.addItem("Methode 1")
        self.comboBox.addItem("Methode 2")
        self.comboBox.addItem("Methode 3")
        
        # used to display the dynamic content of the QComboBox
        self.leftlayout.addWidget(self.comboBox)

        self.dynamic_content_label = QLabel(self)
        self.leftlayout.addWidget(self.dynamic_content_label)
        
        self.setLayout(self.mainlayout)
        
        
        # QPushbutton used to load an image
        # Qlabel used to display the image path
        self.load = QPushButton("Charger une image")
        self.load_label = QLabel("Aucune image chargée")
        self.load_label.setMinimumWidth(300)
        self.leftlayout.addWidget(self.load)
        self.leftlayout.addWidget(self.load_label)
        self.setLayout(self.leftlayout)
        
        # QSpacerItem used to add space between widgets
        self.leftlayout.addItem(spacer)
        
        # QCheckBox used to select the filters
        self.gamma_checkbox = QCheckBox("Gamma")
        self.leftlayout.addWidget(self.gamma_checkbox)
        
        # QSlider used to change the brightness of the image
        self.gamma_widget = SliderWidget(0, 100, 0)
        self.leftlayout.addWidget(self.gamma_widget)
        
        # QSpacerItem used to add space between widgets
        self.leftlayout.addItem(spacer)

        # QCheckBox used to select the filters
        self.saturation_checkbox = QCheckBox("Saturation")
        self.leftlayout.addWidget(self.saturation_checkbox)
    
        # QSlider used to change the saturation of the image
        self.saturation_widget = SliderWidget(0, 100, 0)
        self.leftlayout.addWidget(self.saturation_widget)
        
        # QSpacerItem used to add space between widgets
        self.leftlayout.addItem(spacer)
        
        
        # QCheckBox used to select the filters
        self.blur_checkbox = QCheckBox("Blur")
        self.leftlayout.addWidget(self.blur_checkbox)
        
        self.blur_widget = SliderWidget(0, 100, 0)
        self.leftlayout.addWidget(self.blur_widget)
            
            
        # QPushButton used to generate the image
        self.generate = QPushButton("Générer l'image")
        self.leftlayout.addWidget(self.generate)
        
        
        # right side of the window
        
        # Display the image
        self.image: ImageWidget = ImageWidget()
        self.imageLayout: QVBoxLayout = QVBoxLayout()
        self.image.setLayout(self.imageLayout)
        self.image.setMinimumHeight(500)
        self.image.setMinimumWidth(500)
        self.rightlayout.addWidget(self.image)
        
        # Change the image, previous and next
        self.change = QWidget()
        self.changelayout = QHBoxLayout()
        self.change.setLayout(self.changelayout)
        
        self.previous = QPushButton("Précédent")
        self.previous.setMaximumWidth(100)
        self.changelayout.addWidget(self.previous)
        
        self.next = QPushButton("Suivant")
        self.next.setMaximumWidth(100)
        self.changelayout.addWidget(self.next)
        
        # Add stretch to the layout
        self.rightlayout.addStretch()
        self.leftlayout.addStretch()
        
        
        
        # Add the left and right side to the main layout
        self.mainlayout.addWidget(self.left)
        self.mainlayout.addWidget(self.right)
        
        # Add the widget to the right layout
        self.rightlayout.addWidget(self.change)
        
        # Connecting Callback
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.load.clicked.connect(self.load_image)
        self.gamma_checkbox.stateChanged.connect(self.control_gamma_signal)
        self.saturation_checkbox.stateChanged.connect(self.control_saturation_signal)
        self.blur_checkbox.stateChanged.connect(self.control_blur_signal)
        

        # Initialize signals
        self.control_gamma_signal()
        self.control_saturation_signal()
        self.control_blur_signal()


    # Callback methods
    def control_gamma_signal(self):
        if self.gamma_checkbox.isChecked():
            self.gamma_widget.valueChanged.emit(self.gammaValue)
            self.gammaValue.emit(self.gammaValue)
            self.update_image("gamma")
       
    def control_saturation_signal(self):
        if self.saturation_checkbox.isChecked():
            self.saturation_widget.valueChanged.emit(self.saturationValue)
            self.saturationValue.emit(self.saturationValue)
            self.update_image("saturation")
       
    def control_blur_signal(self):
        if self.blur_checkbox.isChecked():
            self.blur_widget.valueChanged.emit(self.blurValue)
            self.blurValue.emit(self.blurValue)
            
            self.update_image("blur")
    def generate_signal(self):
        self.generate.clicked.emit()
            
        

    # Display different content based on the selected option
    def on_combobox_changed(self, index):
        selected_option = self.comboBox.currentText()

        # Clear previous dynamic content
        self.dynamic_content_label.clear()

        # Show different content based on the selected option
        if selected_option == "Methode 1":
            self.show_method_1_content()
        elif selected_option == "Methode 2":
            self.show_method_2_content()
        elif selected_option == "Methode 3":
            self.show_method_3_content()



    def show_method_1_content(self):
        # Implement the content for Method 1
        self.dynamic_content_label.setText("Explication methode 1")

    def show_method_2_content(self):
        # Implement the content for Method 2
        self.dynamic_content_label.setText("Explication methode 2")

    def show_method_3_content(self):
        # Implement the content for Method 3
        self.dynamic_content_label.setText("Explication methode 3")


    # Load an image
    def load_image(self):
        chemin = QFileDialog.getOpenFileName(self, "Ouvrir une image", "", "Images (*.png *.jpg)")[0]
        if chemin:
            import numpy as np
            from matplotlib.pyplot import imread
            img : np.ndarray = imread(chemin)/255

          
            
            self.load_label.setText(f"Image chargée : {chemin}")
            
            self.image.setPixmap(img)
            
    #TODO: Fonction qui permet d'ajouter ou retirer les décorateurs à l'image
    def update_image(self: Vue_Traitement, decorator):
        print(decorator)
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Vue_Traitement()
    fenetre.show()
    app.exec()
