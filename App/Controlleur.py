import sys
import Vue_Traitement
import Traitement
from PyQt6.QtWidgets import QApplication

class Controlleur:
    def __init__(self):
        
        self.callback = True
    
        self.traitement = Traitement.Traitement()
        self.vue = Vue_Traitement.Vue_Traitement(self)
        