from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class StanzaGUI(QDialog):

    def __init__(self):
        super(StanzaGUI, self).__init__()
        loadUi("GUI/StanzaGUI.ui", self)
