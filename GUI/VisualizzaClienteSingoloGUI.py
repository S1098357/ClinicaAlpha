from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaClienteSingoloGUI(QDialog):

    def __init__(self,cliente):
        super(VisualizzaClienteSingoloGUI, self).__init__()
        loadUi("GUI/VisualizzaClienteGUI.ui", self)
        self.label_2.setText(cliente.nomeCognome)
        self.label_7.setText(cliente.nomeDottore)
        self.label_3.setText(cliente.email)
        self.label_5.setText(cliente.numeroDiTelefono)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None