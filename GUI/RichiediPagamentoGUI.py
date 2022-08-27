from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi



class RichiediPagamentoGUI(QDialog):

    def __init__(self,prezzo):
        super(RichiediPagamentoGUI, self).__init__()
        loadUi("GUI/RichiediPagamentoGUI.ui", self)
        self.label.setText('Prezzo : ' + str(prezzo))