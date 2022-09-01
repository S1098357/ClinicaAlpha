from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class CompilaCertificatoGUI(QDialog):

    def __init__(self,cliente,dottore):
        super(CompilaCertificatoGUI, self).__init__()
        loadUi("GUI/Compila Certificato Medico.ui", self)
        self.label_5.setText(dottore)
        self.lineEdit.setText(cliente)
        self.comboBox.addItems(['certificato agonistico','certificato malattia','certificato sana e robusta costituzione'])

    def stampa(self):
        self.show()
        if self.comboBox.currentText()=='certificato agonistico':
            self.label_6='50.00 €'
        elif self.comboBox.currentText() == 'certificato malattia':
            self.label_6 = '0.00 €'
        else :
            self.label_6 = '100.00 €'
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        if self.label_6=='50.00 €':
            prezzo=50.00
        elif self.label_6=='100.00 €':
            prezzo=100.00
        else:
            prezzo=0.00
        return self.lineEdit.toPlainText(), self.comboBox.currentText(), prezzo

    def indietro(self):
        self.close()
        return None, None,None
