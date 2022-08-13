from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class AggiornaCCGUI(QDialog):

    def __init__(self,patologie):
        super(AggiornaCCGUI, self).__init__()
        loadUi("GUI/AggiornaCC.ui", self)
        self.textEdit.setText(patologie)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        return self.lineEdit.toPlainText()

    def indietro(self):
        self.close()
        return None