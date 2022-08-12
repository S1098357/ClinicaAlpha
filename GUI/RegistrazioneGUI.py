from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class RegistrazioneGUI(QDialog):

    def __init__(self,flag,listaDottori):
        super(RegistrazioneGUI, self).__init__()
        loadUi("GUI/RegistrazioneGUI.ui", self)
        for dottore in listaDottori:
            self.comboBox.addItem(dottore.nomeCognome)
        if flag==True:
            self.label_8='dati inseriti non validi'

    def stampa(self,):
        self.show()
        self.pushButton_2.clicked.connect(self.avanti)

    def avanti(self):
        self.close()
        return self.lineEdit.text(),self.comboBox.currentText(), self.lineEdit_5.text(),self.lineEdit_3.text(),self.lineEdit_2.text(),self.lineEdit_4.text(),self.textEdit.toPlainText()
