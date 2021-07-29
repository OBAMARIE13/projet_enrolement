import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap
from widgets.regist import Registers
from widgets.liste_widgets import Listes

FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/acceuil.ui"))

class Main(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boutons()

    def boutons(self):
        self.btn_regist.clicked.connect(self.register_)
        self.btn_liste.clicked.connect(self.liste_)
        
    def register_(self):
        self.window = Registers()
        self.window.show()
         
    def liste_(self):
        self.window = Listes()
        self.window.show()       
    