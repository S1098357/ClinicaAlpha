from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaRicettaGUI:

    def __init__(self,ricetta):
        super(VisualizzaRicettaGUI, self).__init__()
        loadUi("GUI/VisualizzaRicettaGUI.ui", self)
        self.label_2.setText(ricetta.nomePaziente)
        self.label_4.setText(ricetta.nomeDottore)
        self.label_5.setText(ricetta.dataRilascio)
        self.textBrowser.setText(ricetta.farmacoPrescritto)