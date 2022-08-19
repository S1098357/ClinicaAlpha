from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaClienteSingoloGUI(QDialog):

    def __init__(self,cliente):
        super(VisualizzaClienteSingolo, self).__init__()
        loadUi("GUI/VisualizzaClienteGUI.ui", self)
        self.label_2=cliente.nomeCognome
        self.label_7=cliente.nomeDottore
        self.label_3=cliente.email
        self.label_5=cliente.numeroDiTelefono

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None