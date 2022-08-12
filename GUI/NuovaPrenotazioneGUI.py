from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi



class NuovaPrenotazioneGUI(QDialog):

    def __init__(self,lista1):
        super(NuovaPrenotazioneGUI, self).__init__()
        loadUi("GUI/Prenotazione.ui", self)
        for orario in lista1:
            self.comboBox_2.addItem(orario.strftime('%H:%M'))
        self.comboBox.addItems(['Certificato', 'Ricetta', 'Visita Medica Generica'])
        self.textEdit.toPlainText()
        self.stampa()


    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.chiudiFinestra)
        self.pushButton_2.clicked.connect(self.close)


    def chiudiFinestra(self):
        self.close()
        return self.comboBox_2.currentText(), self.comboBox.currentText(), self.textEdit.toPlainText()

