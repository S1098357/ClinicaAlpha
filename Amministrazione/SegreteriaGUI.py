import datetime
import os.path

from Amministrazione.Segreteria import Segreteria
from Amministrazione.Sistema import Sistema
from Amministrazione.Calendario import Calendario
from Amministrazione.Stanza import Stanza
from Servizio.Cliente import Cliente
from Servizio.Dottore import Dottore
from Servizio.CartellaClinica import CartellaClinica
from Servizio.CertificatoMedico import CertificatoMedico
from Servizio.Documento import Documento
from Servizio.Prenotazione import Prenotazione
from Servizio.Ricetta import Ricetta
from Servizio.Ricevuta import Ricevuta
from GUI.MenuSegreteriaGUI import MenuSegreteriaGUI
from GUI.EliminaCCGUI import EliminaCCGUI
from GUI.VisualizzaEliminaPrenGUI import VisualizzaEliminaPrenGUI
from GUI.VisualizzaTuttePrenotazioniGUI import VisualizzaTuttePrenotazioniGUI
from GUI.EliminaPrenotazioneGUI import EliminaPrenotazioneGUI
from GUI.MenuStampaGUI import MenuStampaGUI
from GUI.StampaRicettaGUI import StampaRicettaGUI
from GUI.StampaCertificatoGUI import StampaCertificatoGUI
from GUI.RichiediPagamentoGUI import RichiediPagamentoGUI
from GUI.RUDClienteGUI import RUDClienteGUI
from GUI.SceltaClienteGUI import SceltaClienteGUI
from GUI.ModificaClienteGUI import ModificaClienteGUI
from GUI.VisualizzaClienteSingoloGUI import VisualizzaClienteSingoloGUI
from GUI.MessaggioGUI import MessaggioGUI
from GUI.RicevutaGUI import RicevutaGUI
from GUI.ModificaOrarioDottoreGUI import ModificaOrarioDottoreGUI
from GUI.MenuStanzeGUI import MenuStanzeGUI
from GUI.StanzaGUI import StanzaGUI
from GUI.VisualizzaRicettaGUI import VisualizzaRicettaGUI
from GUI.VisualizzaCertificatoGUI import VisualizzaCertificatoGUI
from GUI.VisualizzaClienteSingoloGUI import VisualizzaClienteSingoloGUI



class SegreteriaGUI:

    def __init__(self):
        self.segreteria=Segreteria()
        self.segreteria.leggiClienti()
        self.listaClienti=self.segreteria.listaClienti
        self.calendario=Calendario()
        self.sistema=Sistema(self.calendario.Dottori)
        self.listaDottori=self.calendario.Dottori
        self.menu=MenuSegreteriaGUI()
        self.listaId=[]
        for cliente in self.listaClienti:
            self.listaId.append(cliente.id)
        self.listaId=sorted(self.listaId)
        self.eliminaCCGUI=None
        self.VisualizzaEliminaPrenGUI=None
        self.visualizzaListaPrenGUI=None
        self.eliminaPrenGUI=None
        self.menuStampaGUI=None
        self.ricetta=Ricetta()
        self.stampaRicettaGUI=None
        self.certificato=CertificatoMedico()
        self.stampaCertificatoGUI=None
        self.richiediPagamentoGUI=None
        self.RUDClienteGUI=None
        self.sceltaClienteGUI=None
        self.clienteScelto=Cliente()
        self.CCScelta=CartellaClinica(0)
        self.modificaClienteGUI=None
        self.appoggioNome=''
        self.visualizzaClienteGUI=None
        self.MessaggioGUI=None
        self.ricevuta=Ricevuta()
        self.ricevutaGUI=None
        self.modificaOraroDottoreGUI=None
        self.menuStanzeGUI=None
        self.stanzaGUI=None

    def Menu(self):
        self.menu.show()
        self.menu.pushButton.clicked.connect(self.eliminaCC)
        self.menu.pushButton_2.clicked.connect(self.stampaDocumenti)
        self.menu.pushButton_3.clicked.connect(self.visualizzaEliminaPren)
        self.menu.pushButton_4.clicked.connect(self.RUDCliente)
        self.menu.pushButton_5.clicked.connect(self.visualizzaStanze)
        self.menu.pushButton_6.clicked.connect(self.scriviMessaggio)
        self.menu.pushButton_7.clicked.connect(self.richiediPagamento)
        self.menu.pushButton_8.clicked.connect(self.modificaOrarioDottore)

    def chiudiTutto(self):
        if self.eliminaCCGUI!=None:
            self.eliminaCCGUI.close()
        if self.VisualizzaEliminaPrenGUI!=None:
            self.VisualizzaEliminaPrenGUI.close()
        if self.visualizzaListaPrenGUI != None:
            self.visualizzaListaPrenGUI.close()
        if self.eliminaPrenGUI != None:
            self.eliminaPrenGUI.close()
        if self.menuStampaGUI != None:
            self.menuStampaGUI.close()
        if self.stampaRicettaGUI != None:
            self.stampaRicettaGUI.close()
        if self.stampaCertificatoGUI != None:
            self.stampaCertificatoGUI.close()
        if self.richiediPagamentoGUI != None:
            self.richiediPagamentoGUI.close()
        if self.RUDClienteGUI != None:
            self.RUDClienteGUI.close()
        if self.sceltaClienteGUI != None:
            self.sceltaClienteGUI.close()
        if self.modificaClienteGUI != None:
            self.modificaClienteGUI.close()
        if self.visualizzaClienteGUI != None:
            self.visualizzaClienteGUI.close()
        if self.MessaggioGUI != None:
            self.MessaggioGUI.close()
        if self.ricevutaGUI != None:
            self.ricevutaGUI.close()
        if self.modificaOraroDottoreGUI != None:
            self.modificaOraroDottoreGUI.close()
        if self.menuStanzeGUI != None:
            self.menuStanzeGUI.close()
        if self.stanzaGUI != None:
            self.stanzaGUI.close()
        self.menu.show()

    def eliminaCC(self):
        self.menu.hide()
        lista=[]
        for id in self.listaId:
            if os.path.isfile('dati/CC/cartella' + str(id) + '.pickle'):
                lista.append(str(id))
        self.eliminaCCGUI=EliminaCCGUI(lista)
        self.eliminaCCGUI.show()
        self.eliminaCCGUI.pushButton.clicked.connect(self.rimuoviCC)
        self.eliminaCCGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def rimuoviCC(self):
        self.eliminaCCGUI.close()
        self.segreteria.eliminaCartellaClinica(self.eliminaCCGUI.comboBox.currentText())
        self.menu.show()

    def stampaDocumenti(self):
        self.menu.hide()
        self.menuStampaGUI=MenuStampaGUI()
        self.menuStampaGUI.show()
        self.menuStampaGUI.pushButton.clicked.connect(self.stampaRicetta)
        self.menuStampaGUI.pushButton_2.clicked.connect(self.stampaCertificato)
        self.menuStampaGUI.pushButton_3.clicked.connect(self.chiudiTutto)

    def stampaRicetta(self):
        self.menuStampaGUI.hide()
        if self.segreteria.leggiRicetta()!=None:
            self.ricetta=self.segreteria.leggiRicetta()
            self.stampaRicettaGUI = VisualizzaRicettaGUI(self.ricetta)
            self.stampaRicettaGUI.show()
            self.stampaRicettaGUI.pushButton.clicked.connect(self.chiudiTutto)
        else:
            self.chiudiTutto()

    def stampaCertificato(self):
        self.menuStampaGUI.hide()
        if self.segreteria.leggiCertificato() != False:
            self.certificato=self.segreteria.leggiCertificato()
            self.stampaCertificatoGUI=VisualizzaCertificatoGUI(self.certificato)
            if self.certificato.prezzo==50.00:
                self.stampaCertificatoGUI.textBrowser.setText('Si attesta l''idoneità fisica del paziente allo sport agonistico')
            if self.certificato.prezzo==0:
                self.stampaCertificatoGUI.textBrowser.setText('Si attesta lo stato di malattia del paziente')
            else:
                self.stampaCertificatoGUI.textBrowser.setText('Si attesta lo stato di buona salute del paziente')
            self.stampaCertificatoGUI.show()
            self.stampaCertificatoGUI.pushButton.clicked.connect(self.chiudiTutto)
        else:
            self.chiudiTutto()

    def visualizzaEliminaPren(self):
        self.menu.hide()
        self.VisualizzaEliminaPrenGUI=VisualizzaEliminaPrenGUI()
        self.VisualizzaEliminaPrenGUI.show()
        self.VisualizzaEliminaPrenGUI.pushButton.clicked.connect(self.visualizzaPren)
        self.VisualizzaEliminaPrenGUI.pushButton_2.clicked.connect(self.eliminaPren)
        self.VisualizzaEliminaPrenGUI.pushButton_3.clicked.connect(self.chiudiTutto)

    def visualizzaPren(self):
        self.VisualizzaEliminaPrenGUI.close()
        self.visualizzaListaPrenGUI = VisualizzaTuttePrenotazioniGUI(self.sistema.listaPrenotazioni)
        self.visualizzaListaPrenGUI.show()
        self.visualizzaListaPrenGUI.pushButton.clicked.connect(self.chiudiTutto)

    def eliminaPren(self):
        self.VisualizzaEliminaPrenGUI.close()
        lista=[]
        for prenotazione in self.sistema.listaPrenotazioni:
            lista.append(prenotazione.cliente+' , '+ prenotazione.dataOra.strftime('%y-%m-%d %H:%M'))
        self.eliminaPrenGUI=EliminaPrenotazioneGUI(lista)
        self.eliminaPrenGUI.show()
        self.eliminaPrenGUI.pushButton.clicked.connect(self.rimuoviPren)
        self.eliminaPrenGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def rimuoviPren(self):
        appoggio=self.eliminaPrenGUI.comboBox.currentText()
        if appoggio!='':
            self.eliminaPrenGUI.close()
            x,appoggio=appoggio.split(',')
            appoggio=appoggio[1:]
            for prenotazione in self.sistema.listaPrenotazioni:
                if prenotazione.dataOra==datetime.datetime.strptime(appoggio,'%y-%m-%d %H:%M'):
                    self.sistema.listaPrenotazioni.remove(prenotazione)
            self.sistema.salvaPrenotazioni()
            self.menu.show()
        else:
            self.chiudiTutto()

    def richiediPagamento(self):
        self.menu.hide()
        if self.segreteria.leggiCertificato != False:
            self.certificato=self.segreteria.leggiCertificato()
            self.richiediPagamentoGUI=RichiediPagamentoGUI(self.certificato.prezzo)
            self.richiediPagamentoGUI.show()
            self.richiediPagamentoGUI.pushButton.clicked.connect(self.emettiRicevuta)
            self.richiediPagamentoGUI.pushButton_2.clicked.connect(self.chiudiTutto)
        else:
            self.chiudiTutto()

    def emettiRicevuta(self):
        self.ricevuta.prezzo=self.certificato.prezzo
        self.richiediPagamentoGUI.close()
        self.ricevuta.salva(self.ricevuta.prezzo)
        self.ricevutaGUI=RicevutaGUI(self.ricevuta)
        self.ricevutaGUI.show()
        self.ricevutaGUI.pushButton.clicked.connect(self.chiudiTutto)

    def RUDCliente(self):
        self.menu.hide()
        self.RUDClienteGUI=RUDClienteGUI()
        self.RUDClienteGUI.show()
        self.RUDClienteGUI.pushButton.clicked.connect(self.modificaClienteSel)
        self.RUDClienteGUI.pushButton_2.clicked.connect(self.visualizzaClienteSel)
        self.RUDClienteGUI.pushButton_3.clicked.connect(self.eliminaClienteSel)
        self.RUDClienteGUI.pushButton_4.clicked.connect(self.chiudiTutto)

    def modificaClienteSel(self):
        self.RUDClienteGUI.close()
        lista=[]
        for cliente in self.listaClienti:
            lista.append(cliente.nomeCognome)
        self.sceltaClienteGUI=SceltaClienteGUI(lista)
        self.sceltaClienteGUI.show()
        self.sceltaClienteGUI.pushButton.clicked.connect(self.chiudiTutto)
        self.sceltaClienteGUI.pushButton_2.clicked.connect(self.modificaCliente)

    def modificaCliente(self):
        self.appoggioNome=self.sceltaClienteGUI.comboBox.currentText()
        self.sceltaClienteGUI.close()
        for cliente in self.listaClienti:
            if cliente.nomeCognome==self.appoggioNome:
                self.clienteScelto=cliente
        self.CCScelta.id=self.clienteScelto.id
        self.CCScelta.leggiCartella()
        self.modificaClienteGUI=ModificaClienteGUI(self.clienteScelto,self.CCScelta)
        self.modificaClienteGUI.show()
        self.modificaClienteGUI.pushButton.clicked.connect(self.aggiornaCliente)
        self.modificaClienteGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def aggiornaCliente(self):
        self.clienteScelto.nomeCognome=self.modificaClienteGUI.lineEdit.text()
        self.clienteScelto.email=self.modificaClienteGUI.lineEdit_2.text()
        self.clienteScelto.numeroDiTelefono=self.modificaClienteGUI.lineEdit_3.text()
        self.modificaClienteGUI.close()
        for cliente in self.listaClienti:
            if self.appoggioNome==cliente.nomeCognome:
                self.listaClienti.remove(cliente)
                self.listaClienti.append(self.clienteScelto)
        self.segreteria.listaClienti=self.listaClienti
        self.segreteria.salvaClienti()
        self.menu.show()

    def visualizzaClienteSel(self):
        self.RUDClienteGUI.close()
        lista = []
        for cliente in self.listaClienti:
            lista.append(cliente.nomeCognome)
        self.sceltaClienteGUI = SceltaClienteGUI(lista)
        self.sceltaClienteGUI.show()
        self.sceltaClienteGUI.pushButton.clicked.connect(self.chiudiTutto)
        self.sceltaClienteGUI.pushButton_2.clicked.connect(self.visualizzaCliente)

    def visualizzaCliente(self):
        self.appoggioNome = self.sceltaClienteGUI.comboBox.currentText()
        self.sceltaClienteGUI.close()
        for cliente in self.listaClienti:
            if cliente.nomeCognome==self.appoggioNome:
                self.clienteScelto=cliente
        self.visualizzaClienteGUI=VisualizzaClienteSingoloGUI(self.clienteScelto)
        self.visualizzaClienteGUI.show()
        self.visualizzaClienteGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def eliminaClienteSel(self):
        self.RUDClienteGUI.close()
        lista = []
        for cliente in self.listaClienti:
            lista.append(cliente.nomeCognome)
        self.sceltaClienteGUI = SceltaClienteGUI(lista)
        self.sceltaClienteGUI.show()
        self.sceltaClienteGUI.pushButton.clicked.connect(self.chiudiTutto)
        self.sceltaClienteGUI.pushButton_2.clicked.connect(self.eliminaCliente)

    def eliminaCliente(self):
        self.appoggioNome = self.sceltaClienteGUI.comboBox.currentText()
        self.sceltaClienteGUI.close()
        for cliente in self.listaClienti:
            if self.appoggioNome==cliente.nomeCognome:
                self.listaClienti.remove(cliente)
        self.segreteria.listaClienti = self.listaClienti
        self.segreteria.salvaClienti()
        self.menu.show()

    def scriviMessaggio(self):
        self.menu.hide()
        #self.RUDClienteGUI.close()
        lista = []
        for cliente in self.listaClienti:
            lista.append(cliente.nomeCognome)
        lista.insert(0,'invia a tutti')
        self.MessaggioGUI=MessaggioGUI(lista)
        self.MessaggioGUI.show()
        self.MessaggioGUI.pushButton.clicked.connect(self.inviaMessaggio)
        self.MessaggioGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def inviaMessaggio(self):
        if self.MessaggioGUI.comboBox.currentText()!='invia a tutti':
            for cliente in self.listaClienti:
                if cliente.nomeCognome==self.MessaggioGUI.comboBox.currentText():
                    self.clienteScelto=cliente
            self.clienteScelto.salvaMessaggio(self.MessaggioGUI.textEdit.toPlainText())
        else:
            for cliente in self.listaClienti:
                cliente.messaggio.append(self.MessaggioGUI.textEdit.toPlainText())
                cliente.salvaMessaggio(self.MessaggioGUI.textEdit.toPlainText())
        self.MessaggioGUI.close()
        self.menu.show()

    def modificaOrarioDottore(self):
        self.menu.hide()
        lista=[]
        for dottore in self.listaDottori:
            lista.append(dottore.nomeCognome)
        self.modificaOraroDottoreGUI=ModificaOrarioDottoreGUI(lista)
        self.modificaOraroDottoreGUI.show()
        self.modificaOraroDottoreGUI.pushButton.clicked.connect(self.modificaOrario)
        self.modificaOraroDottoreGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def modificaOrario(self):
        '''data,giornoSett=self.modificaOraroDottoreGUI.currentText().split(' ')
        match giornoSett:
            case 'lunedì':
                appoggio = 0
            case 'martedì':
                appoggio = 1
            case 'mercoledì':
                appoggio = 2
            case 'giovedì':
                appoggio = 3
            case 'venerdì':
                appoggio = 4
        for dottore in self.listaDottori:
            if dottore.nomeCognome==self.modificaOraroDottoreGUI.comboBox.currentText():
                dottore.orarioLavoro[appoggio]=datetime.strptime(data,'%m/%d/%Y')
                self.modificaOraroDottoreGUI.close()
                dottore.salvaOrari()
        self.menu.show()'''
        for dottore in self.listaDottori:
            if dottore.nomeCognome==self.modificaOraroDottoreGUI.comboBox.currentText():
                orario=self.modificaOraroDottoreGUI.comboBox_2.currentText()+' '+self.modificaOraroDottoreGUI.comboBox_3.currentText()
                dottore.salvaOrari(orario)
        self.modificaOraroDottoreGUI.close()
        self.menu.show()

    def visualizzaStanze(self):
        self.menu.hide()
        self.menuStanzeGUI=MenuStanzeGUI()
        self.menuStanzeGUI.show()
        self.menuStanzeGUI.pushButton.clicked.connect(self.dettagliStanza1)
        self.menuStanzeGUI.pushButton_2.clicked.connect(self.dettagliStanza2)
        self.menuStanzeGUI.pushButton_3.clicked.connect(self.dettagliStanza3)
        self.menuStanzeGUI.pushButton_4.clicked.connect(self.dettagliStanza4)
        self.menuStanzeGUI.pushButton_5.clicked.connect(self.chiudiTutto)

    def dettagliStanza1(self):
        self.menuStanzeGUI.close()
        self.stanzaGUI=StanzaGUI()
        dataLibera=datetime.datetime.combine(datetime.date.today(),self.listaDottori[0].OrarioLavoro[0])+datetime.timedelta(hours=6)
        orarioLibera=dataLibera.time()
        if datetime.datetime.now().time()>self.listaDottori[0].OrarioLavoro[0] and datetime.datetime.now().time()<orarioLibera:
            self.stanzaGUI.label_2.setText('Occupata')
            self.stanzaGUI.label_3.setText('La stanza si svuoterà alle '+orarioLibera.strftime('%H:%M:%S'))
        else:
            self.stanzaGUI.label_2.setText('Libera')
        self.stanzaGUI.show()
        self.stanzaGUI.pushButton.clicked.connect(self.chiudiTutto)

    def dettagliStanza2(self):
        self.menuStanzeGUI.close()
        self.stanzaGUI=StanzaGUI()
        dataLibera=datetime.datetime.combine(datetime.date.today(),self.listaDottori[1].OrarioLavoro[0])+datetime.timedelta(hours=6)
        orarioLibera=dataLibera.time()
        if datetime.datetime.now().time()>self.listaDottori[1].OrarioLavoro[0] and datetime.datetime.now().time()<orarioLibera:
            self.stanzaGUI.label_2.setText('Occupata')
            self.stanzaGUI.label_3.setText('La stanza si svuoterà alle '+orarioLibera.strftime('%H:%M:%S'))
        else:
            self.stanzaGUI.label_2.setText('Libera')
        self.stanzaGUI.show()
        self.stanzaGUI.pushButton.clicked.connect(self.chiudiTutto)

    def dettagliStanza3(self):
        self.menuStanzeGUI.close()
        self.stanzaGUI=StanzaGUI()
        dataLibera = datetime.datetime.combine(datetime.date.today(),self.listaDottori[2].OrarioLavoro[0]) + datetime.timedelta(hours=6)
        orarioLibera = dataLibera.time()
        if datetime.datetime.now().time()>self.listaDottori[2].OrarioLavoro[0] and datetime.datetime.now().time()<orarioLibera:
            self.stanzaGUI.label_2.setText('Occupata')
            self.stanzaGUI.label_3.setText('La stanza si svuoterà alle '+orarioLibera.strftime('%H:%M:%S'))
        else:
            self.stanzaGUI.label_2.setText('Libera')
        self.stanzaGUI.show()
        self.stanzaGUI.pushButton.clicked.connect(self.chiudiTutto)

    def dettagliStanza4(self):
        self.menuStanzeGUI.close()
        self.stanzaGUI=StanzaGUI()
        dataLibera = datetime.datetime.combine(datetime.date.today(),self.listaDottori[3].OrarioLavoro[0]) + datetime.timedelta(hours=6)
        orarioLibera = dataLibera.time()
        if datetime.datetime.now().time()>self.listaDottori[3].OrarioLavoro[0] and datetime.datetime.now().time()<orarioLibera:
            self.stanzaGUI.label_2.setText('Occupata')
            self.stanzaGUI.label_3.setText('La stanza si svuoterà alle '+orarioLibera.strftime('%H:%M:%S'))
        else:
            self.stanzaGUI.label_2.setText('Libera')
        self.stanzaGUI.show()
        self.stanzaGUI.pushButton.clicked.connect(self.chiudiTutto)




















