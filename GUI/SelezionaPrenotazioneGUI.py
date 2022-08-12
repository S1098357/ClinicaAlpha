from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class SelezionaPrenotazioneGUI(QDialog):

    def __init__(self,listaPrenotazioni):
        super(SelezionaPrenotazioneGUI, self).__init__()
        loadUi("GUI/SelezionaPrenotazioneGUI.ui", self)
        self.lista=listaPrenotazioni
        for prenotazione in listaPrenotazioni:
            self.comboBox.addItem(prenotazione.dataOra.strftime('%y-%m-%d %H:%M'))

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        for prenotazione in self.lista:
            if prenotazione.dataOra==self.comboBox.currentText():
                return prenotazione

    def indietro(self):
        self.close()
        return None