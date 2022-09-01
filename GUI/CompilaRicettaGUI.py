import datetime

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class CompilaRicettaGUI(QDialog):

    def __init__(self,dottore,cliente):
        super(CompilaRicettaGUI, self).__init__()
        loadUi("GUI/CompilaRicetta.ui", self)
        self.label_2.setText(dottore)
        self.label_5.setText(cliente)
        self.label_7.setText(datetime.datetime.today().strftime("%m/%d/%Y, %H:%M:%S"))

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        return self.lineEdit.toPlainText(), self.lineEdit_2.toPlainText()

    def indietro(self):
        return None, None
