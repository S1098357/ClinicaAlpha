from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Amministrazione.Calendario import Calendario
from Amministrazione.Segreteria import Segreteria
from Amministrazione.Sistema import Sistema
from Servizio.Cliente import Cliente
from Servizio.ClienteGUI import ClienteGUI
from Servizio.Dottore import Dottore
from Servizio.DottoreGUI import DottoreGUI
from Amministrazione.SegreteriaGUI import SegreteriaGUI


class LoginGUI(QDialog):

    def __init__(self):
        super(LoginGUI, self).__init__()
        loadUi("GUI/LoginGUI.ui", self)
        self.segreteria = Segreteria()
        self.cliente=Cliente()
        self.clienteGUI = None
        self.dottoreGUI = None
        self.calendario = Calendario()
        self.sistema = Sistema(self.calendario.Dottori)
        self.dottore=Dottore('ciao','aaa')
        self.accesso=None
        self.username=None
        self.password=None
        self.risposta=None
        self.idAttuale=0

    def login(self):
        if self.segreteria.leggiClienti()==False:
            self.clienteGUI=ClienteGUI(self.cliente)
            self.clienteGUI.registrazioneDati()
        else:
            for cliente in self.segreteria.listaClienti:
                if cliente.id>self.idAttuale:
                    self.idAttuale=cliente.id
            self.idAttuale+=1
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
        self.clienteGUI = ClienteGUI(self.cliente,self.idAttuale)
        self.clienteGUI.registrazioneDati()
        self.segreteriaGUI=None

    def prosegui(self):
        if self.username == 'segreteria' and self.password == 'seg':
            self.accesso = 'segreteria'
            self.segreteriaGUI=SegreteriaGUI()
            self.segreteriaGUI.Menu()
        for dottore in self.calendario.Dottori:
            if self.username == dottore.nomeCognome and self.password == 'doc':
                self.accesso = 'dottore'
                self.dottore = dottore
                self.dottoreGUI=DottoreGUI(self.dottore)
                self.dottoreGUI.setUp()
        for cliente in self.segreteria.listaClienti:
            if self.username == cliente.nomeCognome and self.password == cliente.password:
                self.accesso = 'cliente'
                self.cliente = cliente
                self.clienteGUI = ClienteGUI(self.cliente,self.cliente.id)
                self.clienteGUI.menuClienteDati()
        if self.accesso==None:
            self.show()
