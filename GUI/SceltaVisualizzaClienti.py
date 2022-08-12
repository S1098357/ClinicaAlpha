from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI import VisualizzaTuttiClientiGUI


class SceltaVisualizzaClienti(QDialog):

    def __init__(self):
        super(SceltaVisualizzaClienti, self).__init__()
        loadUi("Scelta Visualizza Clienti.ui", self)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(VisualizzaTuttiClientiGUI)
        self.pushButton_2.clicked.connect(SelezionaDottoreGUI)