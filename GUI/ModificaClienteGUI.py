from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class ModificaClienteGUI(QDialog):

    def __init__(self,cliente,cartellaClinica):
        super(ModificaClienteGUI, self).__init__()
        loadUi("GUI/ModificaClienteGUI.ui", self)
        self.lineEdit.setText(cliente.nomeCognome)
        self.lineEdit_2.setText(cliente.email)
        self.lineEdit_3.setText(cliente.numeroDiTelefono)
        self.textEdit.setText(cartellaClinica.patologie)

