from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class EliminaPrenotazioneGUI(QDialog):

    def __init__(self, listaPrenotazioniCliente):
        super(EliminaPrenotazioneGUI,self).__init__()
        loadUi("GUI/EliminaPrenotazione.ui", self)
        self.comboBox.addItems(listaPrenotazioniCliente)


    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.chiudiFinestra)
        self.pushButton_2.clicked.connect(self.close)

    def chiudiFinestra(self):
        self.close()
        return self.comboBox.currentText()
