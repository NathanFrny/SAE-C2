from __future__ import annotations
import sys
import os
import numpy as np
from io import BytesIO
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QComboBox, QSlider, QSpacerItem, QSizePolicy, QCheckBox, QLineEdit
from PyQt6.QtGui import QPixmap, QImage, QIntValidator
from PyQt6.QtCore import Qt, pyqtSignal
from modifiers import Blur, Saturation, Gamma, Image
from gradient import GradientSelector, GradientStrategy, LinearGradient, SubtractGradient
import cv2
from PIL import Image as PILImage
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
        self.comboBox.addItem("Soustraction du gradient")
        self.comboBox.addItem("Gradient linéaire")
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
        self.gamma_widget = SliderWidget(1, 5, 1)
        self.leftlayout.addWidget(self.gamma_widget)
        
        # QSpacerItem used to add space between widgets
        self.leftlayout.addItem(spacer)

        # QCheckBox used to select the filters
        self.saturation_checkbox = QCheckBox("Saturation")
        self.leftlayout.addWidget(self.saturation_checkbox)
    
        # QSlider used to change the saturation of the image
        self.saturation_widget = SliderWidget(0, 5, 0)
        self.leftlayout.addWidget(self.saturation_widget)
        
        # QSpacerItem used to add space between widgets
        self.leftlayout.addItem(spacer)
        
        
        # QCheckBox used to select the filters
        self.blur_checkbox = QCheckBox("Blur")
        self.leftlayout.addWidget(self.blur_checkbox)
        
        self.blur_widget = SliderWidget(1, 5, 1)
        self.leftlayout.addWidget(self.blur_widget)
            
            
        # QPushButton used to generate the image
        self.generate = QPushButton("Générer l'image")
        self.generate.clicked.connect(self.on_generate_clicked)
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
        self.previous.clicked.connect(self.show_previous_image)
        self.next.clicked.connect(self.show_next_image)

        # Initialize the local image that is modified by decorators (Blur, saturation, gamma)
        self.local_image = None

        # Initialize signals
        self.control_gamma_signal()
        self.control_saturation_signal()
        self.control_blur_signal()
        
        # Init var for multiple images
        # Stock the loaded images in a list
        self.loaded_images = []
        self.current_image_index = 0

        # Initialize decorators
        self.gamma_decorator = Gamma(1)
        self.saturation_decorator = Saturation(0)
        self.blur_decorator = Blur(1)

        # Initialize path for new images
        self.path = ""

        # Initialize Gradient subtraction methods
        self.gradient_method: GradientStrategy = None
        self.gradient_selector = GradientSelector()


    # Callback methods
    # signal and update for the gamma filter
    def control_gamma_signal(self):
        if self.gamma_checkbox.isChecked():
            if self.local_image:
                self.local_image = self.local_image.add_decorator(self.gamma_decorator)
                self.update_image(self.gamma_decorator)
                self.gamma_widget.valueChanged.emit(self.gammaValue)
                self.gammaValue.emit(self.gammaValue)
        else:
            if self.local_image:
                self.local_image.remove_decorator(Gamma)
    
    # signal and update for the saturation filter
    def control_saturation_signal(self):
        if self.saturation_checkbox.isChecked():
            if self.local_image:
                self.local_image = self.local_image.add_decorator(self.saturation_decorator)
                self.update_image(self.saturation_decorator)
                self.saturation_widget.valueChanged.emit(self.saturationValue)
                self.saturationValue.emit(self.saturationValue)
        else:
            if self.local_image:
                self.local_image.remove_decorator(Saturation)
            
    # signal and update for the blur filter
    def control_blur_signal(self):
        if self.blur_checkbox.isChecked():
            if self.local_image:
                self.local_image = self.local_image.add_decorator(self.blur_decorator)
                self.update_image(self.blur_decorator)
                self.blur_widget.valueChanged.emit(self.blurValue)
                self.blurValue.emit(self.blurValue)
        else:
            if self.local_image:
                self.local_image.remove_decorator(Blur)
            
    # signal for the generate button
    def generate_signal(self):
        self.generate.clicked.emit()
            
    
    # Display different content based on the selected option
    def on_combobox_changed(self, index):
        selected_option = self.comboBox.currentText()

        # Clear previous dynamic content
        self.dynamic_content_label.clear()

        # Show different content based on the selected option
        if selected_option == "Soustraction du gradient":
            if self.path:
                gradient_path = QFileDialog.getOpenFileName(self, "Ouvrir une image", "", "Images (*.png *.jpg)")[0]
                self.gradient_method = SubtractGradient(self.path, gradient_path)
                self.gradient_selector.method = self.gradient_method
            self.show_method_1_content()
        elif selected_option == "Gradient linéaire":
            if self.path:
                print("linéaire")
                self.gradient_method = LinearGradient(self.path)
                self.gradient_selector.method = self.gradient_method
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
        self.path = QFileDialog.getOpenFileName(self, "Ouvrir une image", "", "Images (*.png *.jpg)")[0]
        self.local_image = Image(self.path)
        if self.gradient_method:
            self.gradient_method.path = self.path
        if self.path:
            from matplotlib.pyplot import imread
            img : np.ndarray = imread(self.path)

            _, ext = os.path.splitext(self.path)

            # convert image to jpg
            if not ext.lower() == '.jpg':
                
                img, temp_path = self.convert_to_jpg(img, self.path, ext)

                self.loaded_images.append(img)
                self.current_image_index = len(self.loaded_images) - 1
                self.load_label.setText(f"Image chargée : {temp_path}")
                self.image.setPixmap(img)
            else:
                self.local_image = Image(self.path)
                img : np.ndarray = imread(self.path) / 255
                self.loaded_images.append(img)
                self.current_image_index = len(self.loaded_images) - 1
                self.load_label.setText(f"Image chargée : {self.path}")
                self.image.setPixmap(img)
            
            
    #Methode use to apply the decorator on the image
    def update_image(self: Vue_Traitement, decorator):
        if self.path:
            self.local_image.apply(decorator)
            img : np.ndarray = self.local_image.image/255
            self.image.setPixmap(img)

    def on_generate_clicked(self: Vue_Traitement):
        if self.gradient_method:
            depolluted_image = self.gradient_selector.method.generate()
            img : np.ndarray = depolluted_image / 255
            self.image.setPixmap(img)

    # Method to select the previous image
    def show_previous_image(self):
        if len(self.loaded_images) > 1:
            self.current_image_index = (self.current_image_index - 1) % len(self.loaded_images)
            self.show_current_image()
    
    # Method to select the next image
    def show_next_image(self):
        if len(self.loaded_images) > 1:
            self.current_image_index = (self.current_image_index + 1) % len(self.loaded_images)
            self.show_current_image()
    
    # Method used to display the current image
    def show_current_image(self):
        self.image.setPixmap(self.loaded_images[self.current_image_index])
    
    def convert_to_jpg(self: Vue_Traitement, img: np.ndarray, path: str, ext: str):
        from matplotlib.pyplot import imread
        img = PILImage.fromarray((img * 255).astype(np.uint8))

        img = img.convert('RGB')

        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        buffer.seek(0)

        temp_path = path.replace(ext, '.jpg')
        with open(temp_path, 'wb') as f:
            f.write(buffer.getvalue())

        _, ext = os.path.splitext(temp_path)
        self.local_image = Image(temp_path)
        img: np.ndarray = imread(temp_path) / 255

        os.remove(temp_path)

        return img, temp_path
                 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Vue_Traitement()
    fenetre.show()
    app.exec()
