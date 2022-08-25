from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaRicettaGUI(QDialog):

    def __init__(self,ricetta):
        super(VisualizzaRicettaGUI, self).__init__()
        loadUi("GUI/VisualizzaRicettaGUI.ui", self)
        self.label_2.setText(ricetta.nomePaziente)
        self.label_4.setText(ricetta.nomeCognomeDottore)
        self.label_5.setText(ricetta.dataRilascio.strftime('%m/%d/%Y'))
        self.textBrowser.setText(ricetta.farmacoPrescritto)