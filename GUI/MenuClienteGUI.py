from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MenuClienteGUI(QDialog):

    def __init__(self):
        super(MenuClienteGUI, self).__init__()
        loadUi("GUI/MenuCliente.ui", self)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.ret0)
        self.pushButton_2.clicked.connect(self.ret1)
        self.pushButton_3.clicked.connect(self.ret2)
        self.pushButton_4.clicked.connect(self.ret3)
        self.pushButton_5.clicked.connect(self.ret4)

    def ret0(self):
        self.close()
        return 0

    def ret1(self):
        self.close()
        return 1

    def ret2(self):
        self.close()
        return 2

    def ret3(self):
        self.close()
        return 3

    def ret4(self):
        self.close()
        return 4