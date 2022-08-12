from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaTuttiClientiGUI(QDialog):

    def __init__(self, listaClienti):
        super(VisualizzaTuttiClientiGUI, self).__init__()
        loadUi("Visualizza Tutti i Clienti.ui", self)
        for cliente in listaClienti:
            lista = cliente + '\n'
        self.textBrowser = lista

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(MenuSegreteriaGUI)