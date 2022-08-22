from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MenuStanzeGUI:

    def __init__(self):
        super(MenuStanzeGUI, self).__init__()
        loadUi("GUI/MenuStanzeGUI.ui", self)
