from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI


class ModificaPrenotazioneGUI(QDialog):

    def __init__(self,listaPrenotazioniCliente, listaDateDisponibili):
        super(ModificaPrenotazioneGUI, self).__init__()
        loadUi("ModificaPrenotazione.ui",self)
        self.comboBox.addItems(listaPrenotazioniCliente)
        self.nuovaPrenotazione = NuovaPrenotazioneGUI(listaDateDisponibili)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.chiudiFinestra)
        self.pushButton_2.clicked.connect(self.close)

    def chiudiFinestra(self):
        self.close()
        self.nuovaPrenotazione.setWindowTitle("Modifica Prenotazione")
        self.nuovaPrenotazione.stampa()
        return self.comboBox.currentText()

    def prenotazioneScelta(self):
        self.show()
        self.pushButton.clicked.connect(self.chiudiFinestra2())
        self.pushButton_2.clicked.connect(self.close)

    def chiudiFinestra2(self):
        self.close()
        return self.comboBox.currentText()
