import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUiType
from widgets.carte import CarteId



FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/liste.ui"))

class Listes(QtWidgets.QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getDatas()
        self.carte_id()
       

    def carte_id(self):
        self.btn_carte.clicked.connect(self.shows_)

    def shows_(self):
        self.window = CarteId()
        self.window.show() 
        


    def getDatas(self):
        db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database.db"))
        c = db.cursor()
        command = """ SELECT * FROM registre  """
        resultat = c.execute(command)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(resultat):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))



    def searchs(self):
        self.btn_search.clicked.connect(self.bouton_search)

    
    def bouton_search(self):
        db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database.db"))
        c = db.cursor()
        texte = self.count_filter_txt.text()

        command = """ SELECT * FROM registre WHERE nom=? AND prenom=? """
        resultat = c.execute(command, texte)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(resultat):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
