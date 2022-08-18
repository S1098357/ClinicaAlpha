from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MenuStampaGUI:

    def __init__(self):
        super(MenuStampaGUI, self).__init__()
        loadUi("GUI/EliminaPrenotazione.ui", self)
