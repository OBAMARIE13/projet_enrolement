# from enrolement.widgets.acceuils import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from widgets.acceuil_widgets import Main


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Main()  
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()