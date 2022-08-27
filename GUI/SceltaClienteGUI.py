from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class SceltaClienteGUI(QDialog):

    def __init__(self,listaClienti):
        super(SceltaClienteGUI, self).__init__()
        loadUi("GUI/SceltaClienteGUI.ui", self)
        self.comboBox.addItems(listaClienti)