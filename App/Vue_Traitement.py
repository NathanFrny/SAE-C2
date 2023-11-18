import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QComboBox, QSlider, QSpacerItem, QSizePolicy, QCheckBox
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import cv2
from ImageWidget import ImageWidget

#class vue affichage interface traitement d'image
class Vue_Traitement(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traitement d'images")
        self.resize(800, 500)
        self.mainlayout = QHBoxLayout()
        
        # left side of the window
        self.left = QWidget()
        self.leftlayout = QVBoxLayout()
        self.left.setLayout(self.leftlayout)
        
        # right side of the window
        self.right = QWidget()
        self.rightlayout = QVBoxLayout()
        self.right.setLayout(self.rightlayout)
        
        # QComboBox used to select the method
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Choisir une méthode")
        self.comboBox.addItem("Methode 1")
        self.comboBox.addItem("Methode 2")
        self.comboBox.addItem("Methode 3")
        
        # used to display the dynamic content of the QComboBox
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
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
        self.load.clicked.connect(self.load_image)
        
        # QSpacerItem used to add space between widgets
        spacer = QSpacerItem(40, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.leftlayout.addItem(spacer)
        
        # QSlider used to change the brightness of the image
        self.gamma_label = QLabel("Gamma")
        self.leftlayout.addWidget(self.gamma_label)
        self.gamma = QSlider()
        self.gamma.setMinimum(0)
        self.gamma.setMaximum(50)
        self.gamma.setOrientation(Qt.Orientation.Horizontal)
        self.gamma.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.gamma.setTickInterval(5)
        self.gamma.setValue(0)
        self.gamma.setSingleStep(1)
        self.gamma.setPageStep(1)
        self.gamma.setTracking(True)
        self.gamma.setSliderPosition(0)
        self.leftlayout.addWidget(self.gamma)
        
        # QSpacerItem used to add space between widgets
        self.leftlayout.addItem(spacer)

        # QCheckBox used to select the filters
        self.saturation = QCheckBox("Saturation")
        self.leftlayout.addWidget(self.saturation)
        
        self.blur = QCheckBox("Blur")
        self.leftlayout.addWidget(self.blur)
        
        
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
        self.rightlayout.addWidget(self.change)


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
            imageload = cv2.imread(chemin)
            imageload = cv2.cvtColor(imageload, cv2.COLOR_BGR2RGB)  
            
            self.label.setText(f"Image chargée : {chemin}")
            
            self.image.setPixmap(imageload)
            
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Vue_Traitement()
    fenetre.show()
    app.exec()
