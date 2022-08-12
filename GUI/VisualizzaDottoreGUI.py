from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaDottoreGUI(QDialog):

    def __init__(self,dottore):
        super(VisualizzaDottoreGUI, self).__init__()
        loadUi("GUI/VisualizzaDottoreGUI.ui", self)
        self.label_4.setText(dottore.nomeCognome)
        self.label_5.setText(dottore.numeroDiTelefono)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None

