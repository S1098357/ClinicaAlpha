from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class RicevutaGUI(QDialog):

    def __init__(self,ricevuta):
        super(RicevutaGUI, self).__init__()
        loadUi("GUI/RicevutaGUI.ui", self)
        if ricevuta.prezzo == 50.00:
            self.label_2.setText('Certificato medico agonistico\n')
        if ricevuta.prezzo == 0:
            self.label_2.setText('Certificato medico di malattia\n')
        else:
            self.label_2.setText('Certificato di sana e \n robusta costituzione')
        self.label_4.setText(str(ricevuta.prezzo))
        self.label_6.setText(ricevuta.dataRilascio.strftime("%m/%d/%Y"))

