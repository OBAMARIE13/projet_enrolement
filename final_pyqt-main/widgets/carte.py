import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUiType



FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/carte.ui"))

class CarteId(QtWidgets.QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cartes()

    


    def cartes(self):
        pass
        # db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database.db"))
        # c = db.cursor()
        # command = """ SELECT * FROM registre  """
        # resultat = c.execute(command)
        # # self.tableWidget.setRowCount(0)
        # for nom in enumerate(resultat):
        #     self.nom_identity.setItem(nom, QtWidgets.QLabelIteme(str(nom)))
        # #     for colum_number, data in enumerate(row_data):
        # #         self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
