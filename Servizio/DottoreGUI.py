import datetime
from Servizio.Cliente import Cliente
from Servizio.Dottore import Dottore
from Servizio.CartellaClinica import CartellaClinica
from Servizio.Ricetta import Ricetta
from Servizio.CertificatoMedico import CertificatoMedico
from Servizio.Prenotazione import Prenotazione
from Amministrazione.Sistema import Sistema
from Amministrazione.Calendario import Calendario
from GUI.MenuDottoreGUI import MenuDottoreGUI
from GUI.VisualizzaTuttePrenotazioniGUI import VisualizzaTuttePrenotazioniGUI
from GUI.VisualizzaCCGUI import VisualizzaCCGUI
from GUI.CompilaCertificatoGUI import CompilaCertificatoGUI
from GUI.CompilaRicettaGUI import CompilaRicettaGUI
from GUI.AggiornaCCGUI import AggiornaCCGUI


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
        self.menu=None
        self.prenotazioneAttuale=None
        self.ricetta=Ricetta()
        self.ricettaGUI=None
        self.CC=CartellaClinica(0)
        self.AggiornaCC=None
        self.VisualizzaCC=None
        self.VisualizzaListaPren=None
        self.CompilaCertificato=None
        self.certificato=CertificatoMedico()

        self.prenotazioneProva=Prenotazione()
        self.prenotazioneProva.dottore=Dottore('Enrico Corradini','3333333333')
        self.prenotazioneProva.dataOra=datetime.datetime(2022,8,13,10,0)
        self.clienteProva=Cliente()
        self.clienteProva.nomeCognome='miao'
        self.clienteProva.id=0
        self.prenotazioneProva.cliente=self.clienteProva

    def setUp(self):
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.dataOra.date==datetime.datetime.today() and prenotazione.dottore==self.nomeCognome:
                self.listaPrenotazioniOggi.append(prenotazione)
        self.listaPrenotazioniOggi.append(self.prenotazioneProva)
        if self.listaPrenotazioniOggi!=[]:
            self.listaPrenotazioniOggi=sorted(self.listaPrenotazioniOggi)
            self.clienteAttuale=self.listaPrenotazioniOggi[0].cliente
            self.prenotazioneAttuale=self.listaPrenotazioniOggi[0]
            self.menu=MenuDottoreGUI(self.clienteAttuale.nomeCognome)
        else:
            self.menu=MenuDottoreGUI(None)
        self.menu.show()
        if self.menu.label.text()!= 'Non ci sono altri appuntamenti':
            self.menu.pushButton.clicked.connect(self.compilaCertificato)
            self.menu.pushButton_2.clicked.connect(self.compilaRicetta)
            self.menu.pushButton_3.clicked.connect(self.aggiornaCC)
            self.menu.pushButton_4.clicked.connect(self.chiamaClienteSucc)
            self.menu.pushButton_5.clicked.connect(self.visualizzaListaPren)
            self.menu.pushButton_6.clicked.connect(self.visualizzaCC)

    def chiamaClienteSucc(self):
        #self.menu.hide()
        for prenotazione in self.listaPrenotazioniOggi:
            if prenotazione==self.prenotazioneAttuale:
                if self.listaPrenotazioniOggi[self.prenotazioneAttuale.index()+1]!=None:
                    self.prenotazioneAttuale=self.listaPrenotazioniOggi[self.prenotazioneAttuale.index()+1]
                    self.clienteAttuale=self.prenotazioneAttuale.cliente
                    self.menu = MenuDottoreGUI(self.clienteAttuale.nomeCognome)
                else:
                    self.prenotazioneAttuale = None
                    self.clienteAttuale = None
                    self.menu=MenuDottoreGUI(None)
        #self.menu.show()

    def compilaRicetta(self):
        self.menu.hide()
        self.ricettaGUI=CompilaRicettaGUI(self.clienteAttuale,self.nomeCognome)
        self.ricettaGUI.show()
        self.ricettaGUI.pushButton.clicked.connect(self.inviaRicettaSegreteria)
        self.ricettaGUI.pushButton_2.clicked.connect(self.menu.show)

    def inviaRicettaSegreteria(self):
        self.ricettaGUI.hide()
        self.ricetta.farmacoPrescritto=self.ricettaGUI.textEdit.text()
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
        if self.CompilaCertificato.comboBox.currentText()=='certificato agonistico':
            self.CompilaCertificato.label_6='50.00 €'
        elif self.CompilaCertificato.comboBox.currentText() == 'certificato malattia':
            self.CompilaCertificato.label_6 = '0.00 €'
        else :
            self.CompilaCertificato.label_6 = '100.00 €'
        self.CompilaCertificato.pushButton.clicked.connect(self.stampaCertificato)
        self.CompilaCertificato.pushButton_2.clicked.connect(self.chiudiTutto)

    def stampaCertificato(self):
        self.CompilaCertificato.hide()
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

