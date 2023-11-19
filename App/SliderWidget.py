from __future__ import annotations
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import pyqtSignal, Qt


class SliderWidget(QWidget):
    """
    A custom widget representing a slider with an associated QLineEdit for input.

    Attributes:
        valueChanged (pyqtSignal): Signal emitted when the slider value changes.

    Methods:
        __init__(self: SliderWidget, valueMin: int = 0, valueMax: int = 100, ValueDefault: int = 0):
            Initializes the SliderWidget with the specified minimum, maximum, and default values.

    """
    valueChanged : pyqtSignal = pyqtSignal(int)
    
    
    #construtor
    def __init__(self: SliderWidget, valueMin : int = 0, valueMax : int = 100, ValueDefault : int = 0):
        """
        Initializes the SliderWidget.

        Args:
            valueMin (int): The minimum value of the slider.
            valueMax (int): The maximum value of the slider.
            ValueDefault (int): The default value of the slider.

        """
        super().__init__()
        
        
    
        
        #attributes:
        self._min : int = valueMin
        self._max : int = valueMax
        self._default : int = ValueDefault
        self.value : int = self._default
        
        
        #layout
        self.topLayout : QHBoxLayout = QHBoxLayout()
        self.setLayout(self.topLayout)

        #slider
        self.slider : QSlider = QSlider()
        self.slider.setRange(self._min, valueMax)
        self.slider.setValue(self._default)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
        
        self.topLayout.addWidget(self.slider)
        
        #ligneEdit
        self.inputText : QLineEdit = QLineEdit((str(self._default)))
        self.inputText.setValidator(QIntValidator())
        self.inputText.setFixedWidth(50)
        self.topLayout.addWidget(self.inputText)


        #connecting callback
        self.slider.valueChanged.connect(self.cb_slider)
        self.inputText.editingFinished.connect(self.cb_text)
        
    #callback methods
    
    #callback slider
    def cb_slider(self: SliderWidget):
        """
        Callback method called when the slider value changes.

        Updates the value attribute and emits the valueChanged signal.

        """
        print("SliderWidget.cb_slider()")
        self.value = self.slider.value()
        self.inputText.setText(str(self.value))
        self.valueChanged.emit(self.value)


    #callback text
    def cb_text(self : SliderWidget):
        """
        Callback method called when the slider value changes.

        Updates the value attribute and emits the valueChanged signal.

        """
        print("SliderWidget.cb_text()")      
        self.value = max(min(int(self.inputText.text()), self._max), self._min)
        self.slider.setValue(self.value)
        self.valueChanged.emit(self.value)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SliderWidget(0, 100, 0)
    window.show()
    sys.exit(app.exec())