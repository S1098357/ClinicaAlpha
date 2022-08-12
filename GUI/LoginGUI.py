from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Amministrazione.Calendario import Calendario
from Amministrazione.Segreteria import Segreteria
from Amministrazione.Sistema import Sistema
from Servizio.Cliente import Cliente
from Servizio.ClienteGUI import ClienteGUI
from Servizio.Dottore import Dottore


class LoginGUI(QDialog):

    def __init__(self):
        super(LoginGUI, self).__init__()
        loadUi("GUI/LoginGUI.ui", self)
        self.segreteria = Segreteria()
        self.cliente=Cliente()
        self.clienteGUI = None
        self.calendario = Calendario()
        self.sistema = Sistema(self.calendario.Dottori)
        self.dottore=Dottore('ciao','aaa')
        self.accesso=None
        self.username=None
        self.password=None
        self.risposta=None

    def login(self):
        if self.segreteria.leggiClienti()==False:
            self.clienteGUI=ClienteGUI(self.cliente)
            self.clienteGUI.registrazioneDati()
        else:
            self.GUI()

    def GUI(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.commandLinkButton.clicked.connect(self.registrazione)

    def avanti(self):
        self.hide()
        self.risposta=True
        self.username=self.lineEdit.text()
        self.password=self.lineEdit_2.text()
        self.prosegui()

    def registrazione(self):
        self.risposta = False
        self.username = None
        self.password = None
        self.accesso = True
        self.hide()
        self.clienteGUI = ClienteGUI(self.cliente)
        self.clienteGUI.registrazioneDati()

    def prosegui(self):
        if self.username == 'segreteria' and self.password == 'seg':
            self.accesso = 'segreteria'
            self.segreteria.menuSegreteria()
        for dottore in self.calendario.Dottori:
            if self.username == dottore.nomeCognome and self.password == 'doc':
                self.accesso = 'dottore'
                self.dottore = dottore
                self.dottore.dottorePre(self.sistema.listaPrenotazioni, self.segreteria.listaClienti)
                self.dottore.menuDottore()
        for cliente in self.segreteria.listaClienti:
            if self.username == cliente.nomeCognome and self.password == cliente.password:
                self.accesso = 'cliente'
                self.cliente = cliente
                self.clienteGUI = ClienteGUI(self.cliente)
                self.clienteGUI.menuClienteDati()
        if self.accesso==None:
            self.show()
