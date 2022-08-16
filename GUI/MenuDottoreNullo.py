from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MenuDottoreNullo(QDialog):

    def __init__(self,):
        super(MenuDottoreNullo, self).__init__()
        loadUi("GUI/Menu Dottore.ui", self)
        self.label.setText('Non ci sono altri appuntamenti')