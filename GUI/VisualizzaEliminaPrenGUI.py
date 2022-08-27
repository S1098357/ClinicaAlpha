from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaEliminaPrenGUI(QDialog):

    def __init__(self):
        super(VisualizzaEliminaPrenGUI, self).__init__()
        loadUi("GUI/VisualizzaEliminaPrenGUI.ui", self)