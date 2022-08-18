from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaTuttePrenotazioniGUI(QDialog):

    def __init__(self, listaPrenotazioni):
        super(VisualizzaTuttePrenotazioniGUI, self).__init__()
        loadUi("GUI/VisualizzaTuttePrenotazioniGUI.ui", self)
        lista=''
        for prenotazione in listaPrenotazioni:
            lista += prenotazione.cliente+' : '+ prenotazione.dataOra.strftime('%y-%m-%d %H:%M') + '\n'
        self.textBrowser.setText(lista)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None