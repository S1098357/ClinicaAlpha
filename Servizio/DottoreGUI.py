import datetime
from Servizio.Cliente import Cliente
from Servizio.Dottore import Dottore
from Servizio.CartellaClinica import CartellaClinica
from Servizio.Ricetta import Ricetta
from Servizio.CertificatoMedico import CertificatoMedico
from Servizio.Prenotazione import Prenotazione
from Servizio.CertificatoMalattia import CertificatoMalattia
from Servizio.CertificatoSanaRobustaCostituzione import CertificatoSanaRobustaCostituzione
from Servizio.CertificatoMedicoAgonistico import CertificatoMedicoAgonistico
from Amministrazione.Sistema import Sistema
from Amministrazione.Calendario import Calendario
from Amministrazione.Segreteria import Segreteria
from GUI.MenuDottoreGUI import MenuDottoreGUI
from GUI.VisualizzaTuttePrenotazioniGUI import VisualizzaTuttePrenotazioniGUI
from GUI.VisualizzaCCGUI import VisualizzaCCGUI
from GUI.CompilaCertificatoGUI import CompilaCertificatoGUI
from GUI.CompilaRicettaGUI import CompilaRicettaGUI
from GUI.AggiornaCCGUI import AggiornaCCGUI
from GUI.MenuDottoreNullo import MenuDottoreNullo


class DottoreGUI:

    def __init__(self,dottore):
        self.documento = dottore.documento
        self.clienteAttuale = Cliente()
        self.listaPrenotazioniOggi = dottore.listaPrenotazioniOggi
        self.nomeCognome = dottore.nomeCognome
        self.numeroDiTelefono = dottore.numeroDiTelefono
        self.calendario=Calendario()
        self.OrarioLavoro = dottore.OrarioLavoro
        self.listaCartelleCliniche = dottore.listaCartelleCliniche
        self.sistema=Sistema(self.calendario.Dottori)
        #self.sistema.leggiPrenotazioni()
        self.menu=None
        self.prenotazioneAttuale=None
        self.ricetta=Ricetta()
        self.ricettaGUI=None
        self.CC=CartellaClinica(0)
        self.AggiornaCC=None
        self.VisualizzaCC=None
        self.VisualizzaListaPren=None
        self.CompilaCertificato=None
        self.certificato=None
        self.tipoCertificato=''
        self.segreteria=Segreteria()
        self.segreteria.leggiClienti()
        self.menuNullo=MenuDottoreNullo()

        #self.prenotazioneProva=Prenotazione()
        #self.prenotazioneProva.dottore=Dottore('Enrico Corradini','3333333333')
        #self.prenotazioneProva.dataOra=datetime.datetime(2022,8,13,10,0)
        #self.clienteProva=Cliente()
        #self.clienteProva.nomeCognome='miao'
        #self.clienteProva.id=0
        #self.prenotazioneProva.cliente=self.clienteProva

    def setUp(self):
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.dataOra.date()==datetime.date.today() and prenotazione.dottore==self.nomeCognome:
                self.listaPrenotazioniOggi.append(prenotazione)
        #self.listaPrenotazioniOggi.append(self.prenotazioneProva)
        if self.listaPrenotazioniOggi!=[]:
            listaOrari=[]
            listaOrdinata=[]
            for prenotazione in self.listaPrenotazioniOggi:
                listaOrari.append(prenotazione.dataOra.time())
                listaOrari=sorted(listaOrari)
            for orario in listaOrari:
                for prenotazione in self.listaPrenotazioniOggi:
                    if prenotazione.dataOra.time()==orario:
                        listaOrdinata.append(prenotazione)
            self.listaPrenotazioniOggi=listaOrdinata
            for cliente in self.segreteria.listaClienti:
                if self.listaPrenotazioniOggi[0].cliente==cliente.nomeCognome:
                    self.clienteAttuale=cliente
            #self.listaPrenotazioniOggi=sorted(self.listaPrenotazioniOggi)
            self.prenotazioneAttuale=self.listaPrenotazioniOggi[0]
            self.menu=MenuDottoreGUI(self.prenotazioneAttuale.cliente,self.prenotazioneAttuale.note)
            self.Menu()
        else:
            self.menuNullo.show()

    def Menu(self):
        self.menu.show()
        self.menu.pushButton.clicked.connect(self.compilaCertificato)
        self.menu.pushButton_2.clicked.connect(self.compilaRicetta)
        self.menu.pushButton_3.clicked.connect(self.aggiornaCC)
        self.menu.pushButton_4.clicked.connect(self.chiamaClienteSucc)
        self.menu.pushButton_5.clicked.connect(self.visualizzaListaPren)
        self.menu.pushButton_6.clicked.connect(self.visualizzaCC)

    def chiamaClienteSucc(self):
        self.menu.hide()
        if self.listaPrenotazioniOggi.index(self.prenotazioneAttuale)+1!=len(self.listaPrenotazioniOggi):
            self.prenotazioneAttuale=self.listaPrenotazioniOggi[self.listaPrenotazioniOggi.index(self.prenotazioneAttuale)+1]
            for cliente in self.segreteria.listaClienti:
                if self.prenotazioneAttuale.cliente == cliente.nomeCognome:
                    self.clienteAttuale = cliente
            self.menu.label.setText('Cliente attuale:'+self.prenotazioneAttuale.cliente)
            self.menu.label_2.setText('note: '+self.prenotazioneAttuale.note)
            self.menu.show()
        else:
            self.prenotazioneAttuale = None
            self.clienteAttuale = None
            self.menuNullo.show()

    def compilaRicetta(self):
        self.menu.hide()
        self.ricettaGUI=CompilaRicettaGUI(self.clienteAttuale.nomeCognome,self.nomeCognome)
        self.ricettaGUI.show()
        self.ricettaGUI.pushButton.clicked.connect(self.inviaRicettaSegreteria)
        self.ricettaGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def inviaRicettaSegreteria(self):
        self.ricettaGUI.hide()
        self.ricetta.compilaRicetta(self.ricettaGUI.textEdit.toPlainText(),self.clienteAttuale.nomeCognome,self.nomeCognome,datetime.datetime.now())
        self.ricetta.stampaRicetta()
        self.menu.show()

    def aggiornaCC(self):
        self.CC.id=self.clienteAttuale.id
        self.CC.patologie=self.CC.leggiCartella().get('patologie')
        self.AggiornaCC=AggiornaCCGUI(self.CC.patologie)
        self.AggiornaCC.show()
        self.AggiornaCC.pushButton.clicked.connect(self.modificaCartella)

    def modificaCartella(self):
        self.AggiornaCC.hide()
        self.CC.patologie=self.AggiornaCC.textEdit.toPlainText()
        self.CC.stampaCartella()
        self.menu.show()

    def visualizzaCC(self):
        self.CC.id = self.clienteAttuale.id
        self.CC.patologie = self.CC.leggiCartella().get('patologie')
        self.VisualizzaCC=VisualizzaCCGUI(self.CC.patologie,self.clienteAttuale.nomeCognome)
        self.VisualizzaCC.show()
        self.VisualizzaCC.pushButton.clicked.connect(self.chiudiTutto)

    def visualizzaListaPren(self):
        self.menu.hide()
        self.VisualizzaListaPren=VisualizzaTuttePrenotazioniGUI(self.listaPrenotazioniOggi)
        self.VisualizzaListaPren.show()
        self.VisualizzaListaPren.pushButton.clicked.connect(self.chiudiTutto)

    def compilaCertificato(self):
        self.CompilaCertificato=CompilaCertificatoGUI(self.clienteAttuale.nomeCognome,self.nomeCognome)
        self.CompilaCertificato.show()
        self.CompilaCertificato.pushButton.clicked.connect(self.stampaCertificato)
        self.CompilaCertificato.pushButton_2.clicked.connect(self.chiudiTutto)

    def stampaCertificato(self):
        self.CompilaCertificato.hide()
        self.tipoCertificato = self.CompilaCertificato.comboBox.currentText()
        if self.tipoCertificato=='certificato agonistico':
            self.certificato=CertificatoMedicoAgonistico()
        if self.tipoCertificato=='certificato malattia':
            self.certificato=CertificatoMalattia()
        else:
            self.certificato=CertificatoSanaRobustaCostituzione()
        self.certificato.compilaCertificato(self.clienteAttuale.nomeCognome,self.nomeCognome,datetime.datetime.today())
        self.certificato.stampaCertificato()
        self.menu.show()

    def chiudiTutto(self):
        if self.AggiornaCC!=None:
            self.AggiornaCC.hide()
        if self.VisualizzaCC != None:
            self.VisualizzaCC.hide()
        if self.VisualizzaListaPren != None:
            self.VisualizzaListaPren.hide()
        if self.CompilaCertificato != None:
            self.CompilaCertificato.hide()
        if self.ricettaGUI != None:
            self.ricettaGUI.hide()
        self.menu.show()

