from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MessaggioGUI(QDialog):

    def __init__(self,listaClienti):
        super(MessaggioGUI, self).__init__()
        loadUi("GUI/MessaggioGUI.ui", self)
        self.comboBox.addItems(listaClienti)

