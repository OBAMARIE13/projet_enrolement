import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QRadioButton



FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/registration.ui"))


class Registers(QtWidgets.QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boutons()


    def boutons(self):
        self.btn_envoi_2.clicked.connect(self.enregistrement)
        self.btn_photo.clicked.connect(self.get_image_file)
        self.btn_annuler_2.clicked.connect(self.closeWidget)


    def get_image_file(self):
        file_name,_ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image File', r"C:\\Users\\Ouattara oba", "Image file(*.jpg *.jpeg *.gif)")
        self.photo_label.setPixmap(QtGui.QPixmap(file_name))
        self.photo_label.setScaledContents(True)


    def enregistrement(self):
        nom = self.nom.text()
        prenom = self.prenom.text()
        dates = self.date.text()
        lieu = self.lieu.text()
        domicile = self.domicile.text()
        nom_pere = self.nom_pere_2.text()
        nom_mere = self.nom_mere_2.text()
        nationnalite = self.pays.text()
        sexe = self.sexe_h.isChecked()

        if sexe:
            genre = "M"
        else:
            genre = "F"



        
        if not nom or not prenom or not dates or not nom_pere or not domicile or not nom_mere or not nationnalite or not lieu or not genre:
            QtWidgets.QMessageBox.warning(self, "Error", "Remplissez les champs vides svp")
        
        # else:
        #     db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database"))
        #     c = db.cursor()
        #     command = """ SELECT * FROM registre WHERE nom=? AND prenom=? """
        #     resultat = c.execute(command, (nom, prenom))
            
        #     if resultat.fetchone():
        #         QtWidgets.QMessageBox.warning(self, "Error", "Vous etes déja enrolé")
        else:
            QtWidgets.QMessageBox.information(self, "Success", "Message envoyé avec succès")
            db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database.db"))
            c = db.cursor()
            valeur = (nom, prenom, dates, lieu, domicile, nationnalite, genre, nom_pere, nom_mere)
            c.execute("""INSERT INTO registre (nom, prenom, date, lieu, domicile, nationnalité, genre, nom_pere, nom_mere) VALUES (?,?,?,?,?,?,?,?,?)""", valeur)
            db.commit()
            print(self.photo_label)
            self.nom.clear()
            self.prenom.clear()
            self.date.clear()
            self.nom_pere_2.clear()
            self.nom_mere_2.clear()
            self.domicile.clear()
            self.pays.clear()
            self.lieu.clear()
            self.sexe_f.setChecked(False)
            self.sexe_h.setChecked(True)

           

                
                

   


# def search(self):
#     db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database/data.db"))
#     c = db.cursor()
#     noms = str(self.nom_filter_txt.text())
#     command = """ SELECT * FROM regist WHERE nom=? AND prenom=? """
#     resultat = c.execute(command, (noms))

    def closeWidget(self):
        self.close()



