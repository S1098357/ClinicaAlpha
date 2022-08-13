from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaCCGUI(QDialog):

    def __init__(self,patologie,cliente):
        super(VisualizzaCCGUI, self).__init__()
        loadUi("GUI/VisualizzaCC.ui", self)
        self.label_2.setText(cliente)
        self.textBrowser.setText(patologie)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None
