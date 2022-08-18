from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaCertificatoGUI:

    def __init__(self,certificato):
        super(VisualizzaCertificatoGUI, self).__init__()
        loadUi("GUI/VisualizzaCertificatoGUI.ui", self)
        self.label_2.setText(certificato.nomePaziente)
        self.label_4.setText(certificato.nomeDottore)
        self.label_5.setText(certificato.dataRilascio)
        self.label_9.setText(certificato.prezzo)