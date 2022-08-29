from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class LeggiMessaggioGUI(QDialog):

    def __init__(self,messaggio):
        super(LeggiMessaggioGUI, self).__init__()
        loadUi("GUI/LeggiMessaggioGUI.ui", self)
        self.label_2.setText(messaggio)
