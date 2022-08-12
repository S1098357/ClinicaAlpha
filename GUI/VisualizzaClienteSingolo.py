from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaClienteSingolo(QDialog):

    def __init__(self,cliente):
        super(VisualizzaClienteSingolo, self).__init__()
        loadUi("Visualizza Cliente Singolo.ui", self)
        self.label_8=cliente.nomeCognome
        self.label_9=cliente.nomeDottore
        self.label_10=cliente.email
        self.label_11=cliente.numeroDiTelefono
        self.label_12=cliente.codiceFiscale
        self.label_13=cliente.id


    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(MenuSegreteriaGUI)