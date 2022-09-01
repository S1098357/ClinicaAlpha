import datetime

from Amministrazione.Calendario import Calendario
from Amministrazione.Segreteria import Segreteria

from Amministrazione.Sistema import Sistema
from GUI.VisualizzaDottoreGUI import VisualizzaDottoreGUI
from GUI.VisualizzaTuttePrenotazioniGUI import VisualizzaTuttePrenotazioniGUI
from GUI.MenuClienteGUI import MenuClienteGUI
from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI
from GUI.RegistrazioneGUI import RegistrazioneGUI
from GUI.SelezionaGiornoGUI import SelezionaGiornoGUI
from GUI.SelezionaPrenotazioneGUI import SelezionaPrenotazioneGUI
from Servizio.CartellaClinica import CartellaClinica
from Servizio.Cliente import Cliente
from Servizio.Prenotazione import Prenotazione
from GUI.LeggiMessaggioGUI import LeggiMessaggioGUI
from GUI.UltimoMessaggioGUI import UltimoMessaggioGUI


class ClienteGUI:

    def __init__(self,cliente,id):
        self.nomeCognome = cliente.nomeCognome
        self.nomeDottore = cliente.nomeDottore
        self.password = cliente.password
        self.email = cliente.email
        self.numeroDiTelefono = cliente.numeroDiTelefono
        self.codiceFiscale = cliente.codiceFiscale
        self.id = id
        self.dottore=None
        self.prenotazione=Prenotazione()
        self.messaggioGUI=None
#        self.messaggio = cliente.messaggio
#        self.prenotazione = cliente.prenotazione
       # self.promemoria = cliente.promemoria
        self.listaPrenotazioniCliente = cliente.listaPrenotazioniCliente
        self.calendario = Calendario()
        self.sistema = Sistema(self.calendario.Dottori)
        self.segreteria=Segreteria()
        self.segreteria.leggiClienti()
        self.CC=CartellaClinica(self.id)
        self.cliente=Cliente()
        self.risposta=None
        self.menu = MenuClienteGUI()
        self.appoggio=None
        self.appoggioPrenotazione=None
        self.appoggioDatetime=datetime.datetime
        self.nuovaPrenotazioneGUI=None
        #self.selezionaPrenotazione = SelezionaPrenotazioneGUI(self.sistema.listaPrenotazioni)
        self.selezionaPrenotazione=None
        self.reg=RegistrazioneGUI(False,self.calendario.Dottori)
        self.visualizzaListaPren=None
        if self.nomeDottore!='':
            for dottore in self.sistema.listaDottori:
                if dottore.nomeCognome == self.nomeDottore:
                    self.dottore = dottore
        #self.reg2 = RegistrazioneGUI(True)
        i=0
        lista=[]
        giorno=None
        appoggio=None
        from datetime import date,timedelta
        while i<7:
            giorno=(date.today()+timedelta(days=i))
            if giorno.weekday()!=6 and giorno.weekday()!=5:
                if giorno.weekday() == 0:
                    appoggio = 'Lunedì'
                elif giorno.weekday() == 1:
                    appoggio = 'Martedì'
                elif giorno.weekday() == 2:
                    appoggio = 'Mercoledì'
                elif giorno.weekday() == 3:
                    appoggio = 'Giovedì'
                elif giorno.weekday() == 4:
                    appoggio = 'Venerdì'

                lista.append(giorno.strftime('%y-%m-%d')+' '+appoggio)
            i+=1
        self.selezionaGiorno=SelezionaGiornoGUI(lista)
        '''lista = []
        for dottore in self.sistema.listaDottori:
            if dottore.nomeCognome == self.nomeDottore:
                lista.append(dottore.orarioLavoro[self.appoggioDatetime.weekday()])
        for k in range(0, 23):
            lista.append(lista[len(lista) -1] + timedelta(minutes=15))
        listaPrenotate = []
        for prenotazione in self.sistema.listaPrenotazioni:
            listaPrenotate.append(prenotazione.dataOra)
        # listaFinale = lista - listaPrenotate
        differenza1 = set(lista).difference(set(listaPrenotate))
        differenza2 = set(listaPrenotate).difference(set(lista))
        self.listaFinale = list(differenza1.union(differenza2))
        #self.nuovaPrenotazioneGUI = NuovaPrenotazioneGUI(self.listaFinale)'''

    def registrazioneDati(self):
        self.reg.show()
        self.reg.pushButton_2.clicked.connect(self.registrazioneAvanti)

    def registrazioneAvanti(self):
        self.nomeCognome= self.reg.lineEdit.text()
        self.nomeDottore = self.reg.comboBox.currentText()
        self.password = self.reg.lineEdit_5.text()
        self.email = self.reg.lineEdit_3.text()
        self.numeroDiTelefono = self.reg.lineEdit_2.text()
        self.codiceFiscale = self.reg.lineEdit_4.text()
        self.CC.patologie = self.reg.textEdit.toPlainText()
        self.reg.hide()
        self.cliente.id=self.id
        #self.reg.close()
        if self.cliente.inserisciEmail(self.email)==True and self.cliente.inserisciNumeroDiTelefono(self.numeroDiTelefono)==True and self.cliente.inserisciCodiceFiscale(self.codiceFiscale)==True and self.cliente.inserisciNomeCognome(self.nomeCognome)==True:
            self.CC.stampaCartella()
            self.cliente.inserisciPassword(self.password)
            self.cliente.selezionaMedico(self.nomeDottore)
            for dottore in self.sistema.listaDottori:
                if dottore.nomeCognome==self.nomeDottore:
                    self.dottore=dottore
            self.segreteria.listaClienti.append(self.cliente)
            self.segreteria.salvaClienti()
            self.menuClienteDati()
        else:
            self.reg.show()

    def messaggio(self):
        self.cliente.nomeCognome=self.nomeCognome
        self.cliente.leggiMessaggio()
        if self.cliente.messaggio!=[]:
            self.messaggioGUI=UltimoMessaggioGUI(self.cliente.messaggio)
            self.messaggioGUI.show()
            self.cliente.svuotaMessaggi()
            self.messaggioGUI.pushButton.clicked.connect(self.menuClienteDati)
        else:
            self.menuClienteDati()

    def menuClienteDati(self):
        '''for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.cliente==self.nomeCognome:
                self.listaPrenotazioniCliente.append(prenotazione)'''
        if self.messaggioGUI!=None:
            self.messaggioGUI.close()
        self.menu.show()
        self.menu.pushButton.clicked.connect(self.ret0)
        self.menu.pushButton_2.clicked.connect(self.ret1)
        self.menu.pushButton_3.clicked.connect(self.ret2)
        self.menu.pushButton_4.clicked.connect(self.ret3)
        self.menu.pushButton_5.clicked.connect(self.ret4)

    def ret0(self):
        self.appoggio=None
        self.appoggioDatetime=None
        self.prenotazione=Prenotazione()
        self.listaPrenotazioniCliente=[]
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.cliente==self.nomeCognome:
                self.listaPrenotazioniCliente.append(prenotazione)
        self.menu.hide()
        self.risposta=0
        self.scelta()

    def ret1(self):
        self.appoggio = None
        self.appoggioDatetime = None
        self.prenotazione = Prenotazione()
        self.listaPrenotazioniCliente = []
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.cliente==self.nomeCognome:
                self.listaPrenotazioniCliente.append(prenotazione)
        self.menu.hide()
        self.risposta = 1
        self.scelta()

    def ret2(self):
        self.appoggio = None
        self.appoggioDatetime = None
        self.prenotazione = Prenotazione()
        self.listaPrenotazioniCliente = []
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.cliente==self.nomeCognome:
                self.listaPrenotazioniCliente.append(prenotazione)
        self.menu.hide()
        self.risposta = 2
        self.scelta()

    def ret3(self):
        self.appoggio = None
        self.appoggioDatetime = None
        self.prenotazione = Prenotazione()
        self.listaPrenotazioniCliente = []
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.cliente==self.nomeCognome:
                self.listaPrenotazioniCliente.append(prenotazione)
        self.menu.hide()
        self.risposta = 3
        self.scelta()

    def ret4(self):
        self.appoggio = None
        self.appoggioDatetime = None
        self.prenotazione = Prenotazione()
        self.listaPrenotazioniCliente = []
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.cliente==self.nomeCognome:
                self.listaPrenotazioniCliente.append(prenotazione)
        self.menu.hide()
        self.risposta = 4
        self.scelta()

    def scelta(self):
        match self.risposta:
            case 0:
                self.selezionaGiornoDati()
            case 1:
                self.selezionaPrenotazioneDatiElimina()
            case 2:
                self.selezionaPrenotazioneDatiModifica()
                #self.eliminaPrenotazione(prenotazione, self.sistema)
            case 3:
                self.visualizzaListaPren = VisualizzaTuttePrenotazioniGUI(self.listaPrenotazioniCliente)
                self.visualizzaTutteDati()
            case 4:
                self.visualizzaDottore=VisualizzaDottoreGUI(self.dottore)
                self.visualizzaInfoMedicoDati()


    def richiediPrenotazione(self, listaPrenotazioni, listaDottori):
        #self.prenotazione = Prenotazione
        #delta = datetime.time(minute=15)
        lista=[]
        for dottore in listaDottori:
            if dottore.nomeCognome == self.nomeDottore:
                dottore.leggiOrari()
                lista.append(datetime.datetime.combine(self.appoggioDatetime.date(),dottore.OrarioLavoro[self.appoggio]))
        k=0
        while k <= 23:
            minTot = lista[k].hour * 60 + lista[k].minute
            minTot += 15
            lista.append(datetime.datetime.combine(self.appoggioDatetime.date(),datetime.time(minTot // 60, (minTot % 60))))
            k+=1
        listaPrenotate = []
        for prenotazione in listaPrenotazioni:
            #print(prenotazione.dataOra.date(),self.appoggioDatetime.date())
            if prenotazione.dataOra.date() == self.appoggioDatetime.date():
                listaPrenotate.append(prenotazione.dataOra)
        listaFinale=list(set(lista)-set(listaPrenotate))
        listaFinale=sorted(listaFinale)
        #pren =self.prenotazione()
        self.nuovaPrenotazioneGUI = NuovaPrenotazioneGUI(listaFinale)
        self.nuovaPrenotazioneDati()


        '''if self.prenotazione.dataOra!=None and self.prenotazione.note!=None and self.prenotazione.tipo!=None:
            if self.prenotazione.tipo=='Certificato':
                self.prenotazione.certificatoMedico = True
            elif self.prenotazione.tipo=='Ricetta':
                self.prenotazione.ricettaMedica=True
            else:
                self.prenotazione.visitaGenerica= True
            self.prenotazione.cliente=self.nomeCognome
            self.prenotazione.dottore=self.nomeDottore
            self.sistema.listaPrenotazioni.append(self.prenotazione)
            self.sistema.salvaPrenotazioni()
        self.menuCliente()'''

    def selezionaGiornoDati(self):
        self.selezionaGiorno.show()
        self.selezionaGiorno.pushButton.clicked.connect(self.selezionaGiornoOK)
        self.selezionaGiorno.pushButton_2.clicked.connect(self.selezionaGiornoIndietro)

    def selezionaGiornoOK(self):
        from datetime import datetime
        self.selezionaGiorno.close()
        giorno,scarto=self.selezionaGiorno.comboBox.currentText().split(' ')
        self.appoggioDatetime=datetime.strptime(giorno,'%y-%m-%d')
        if self.appoggioDatetime.weekday()>datetime.now().weekday():
            self.appoggio=self.appoggioDatetime.weekday()-datetime.now().weekday()
        else:
            self.appoggio=datetime.now().weekday()-self.appoggioDatetime.weekday()+2
        self.richiediPrenotazione(self.sistema.listaPrenotazioni, self.sistema.listaDottori)

    def selezionaGiornoIndietro(self):
        self.selezionaGiorno.close()
        #self.appoggioDatetime=None
        self.menu.show()


    def nuovaPrenotazioneDati(self):
        self.nuovaPrenotazioneGUI.show()
        self.nuovaPrenotazioneGUI.pushButton.clicked.connect(self.nuovaPrenotazioneOK)
        self.nuovaPrenotazioneGUI.pushButton_2.clicked.connect(self.nuovaPrenotazioneIndietro)

    def nuovaPrenotazioneOK(self):
        from datetime import datetime
        #ora=datetime.strptime(self.nuovaPrenotazioneGUI.comboBox_2.currentText(),'%H:%M')
        ora=self.appoggioDatetime.strftime('%y-%m-%d')+' '+self.nuovaPrenotazioneGUI.comboBox_2.currentText()
        self.prenotazione.dataOra=datetime.strptime(ora,'%y-%m-%d %H:%M')
        self.prenotazione.tipo = self.nuovaPrenotazioneGUI.comboBox.currentText()
        self.prenotazione.note=self.nuovaPrenotazioneGUI.textEdit.toPlainText()
        self.prenotazione.cliente=self.nomeCognome
        self.eliminaPrenotazione(self.appoggioPrenotazione,self.sistema)
        self.nuovaPrenotazioneGUI.close()
        self.nuovaPrenotazioneProsegui()

    def nuovaPrenotazioneIndietro(self):
        self.prenotazione.dataOra = None
        self.prenotazione.tipo = None
        self.prenotazione.note = None
        self.nuovaPrenotazioneGUI.close()
        self.menu.show()

    def nuovaPrenotazioneProsegui(self):
        if self.prenotazione.dataOra!=None and self.prenotazione.note!=None and self.prenotazione.tipo!=None:
            if self.prenotazione.tipo=='Certificato':
                self.prenotazione.certificatoMedico = True
            elif self.prenotazione.tipo=='Ricetta':
                self.prenotazione.ricettaMedica=True
            else:
                self.prenotazione.visitaGenerica= True
            self.prenotazione.cliente=self.nomeCognome
            self.prenotazione.dottore=self.nomeDottore
            self.sistema.listaPrenotazioni.append(self.prenotazione)
            self.sistema.salvaPrenotazioni()
        self.menu.show()

    def selezionaPrenotazioneDatiElimina(self):
        self.selezionaPrenotazione = SelezionaPrenotazioneGUI(self.listaPrenotazioniCliente)
        self.selezionaPrenotazione.show()
        self.selezionaPrenotazione.pushButton.clicked.connect(self.selezionaPrenotazioneOK)
        self.selezionaPrenotazione.pushButton_2.clicked.connect(self.selezionaPrenotazioneIndietro)

    def selezionaPrenotazioneOK(self):
        from datetime import datetime
        if self.sistema.listaPrenotazioni != []:
            for prenotazione in self.selezionaPrenotazione.lista:
                if prenotazione.dataOra == datetime.strptime(self.selezionaPrenotazione.comboBox.currentText(),'%y-%m-%d %H:%M'):
                    self.prenotazione=prenotazione
            self.selezionaPrenotazione.close()
            self.eliminaPrenotazione(self.prenotazione, self.sistema)
        else:
            self.selezionaPrenotazione.close()
            self.menu.show()

    def selezionaPrenotazioneIndietro(self):
        self.prenotazione=None
        self.selezionaPrenotazione.close()
        self.menu.show()

    def eliminaPrenotazione(self,prenotazione,sistema):
        for elem in sistema.listaPrenotazioni:
            if elem==prenotazione:
                sistema.listaPrenotazioni.remove(prenotazione)
                self.listaPrenotazioniCliente.remove(prenotazione)
        sistema.salvaPrenotazioni()
        self.menu.show()

    def selezionaPrenotazioneDatiModifica(self):
        self.selezionaPrenotazione = SelezionaPrenotazioneGUI(self.listaPrenotazioniCliente)
        self.selezionaPrenotazione.show()
        self.selezionaPrenotazione.pushButton.clicked.connect(self.selezionaPrenotazioneModificaOK)
        self.selezionaPrenotazione.pushButton_2.clicked.connect(self.selezionaPrenotazioneModificaIndietro)

    def selezionaPrenotazioneModificaOK(self):
        from datetime import datetime
        if self.selezionaPrenotazione.lista==[]:
            self.selezionaPrenotazione.close()
            self.menu.show()
        else:
            for prenotazione in self.selezionaPrenotazione.lista:
                if prenotazione.dataOra == datetime.strptime(self.selezionaPrenotazione.comboBox.currentText(),'%y-%m-%d %H:%M'):
                    #self.prenotazione=prenotazione
                    self.appoggioPrenotazione=prenotazione
            self.selezionaPrenotazione.close()
            self.selezionaGiornoDati()
        #self.menuClienteDati()

    def selezionaPrenotazioneModificaIndietro(self):
        self.prenotazione=None
        self.selezionaPrenotazione.close()
        self.menu.show()

    def eliminaPrenotazioneModifica(self,prenotazione,sistema):
        for elem in sistema.listaPrenotazioni:
            if elem==prenotazione:
                sistema.listaPrenotazioni.remove(prenotazione)
                self.listaPrenotazioniCliente.remove(prenotazione)
        sistema.salvaPrenotazioni()
        self.selezionaGiornoDati()

    def visualizzaTutteDati(self):
        self.visualizzaListaPren.show()
        self.visualizzaListaPren.pushButton.clicked.connect(self.visualizzaTutteIndietro)

    def visualizzaTutteIndietro(self):
        self.visualizzaListaPren.close()
        self.menu.show()

    def visualizzaInfoMedicoDati(self):
        self.visualizzaDottore.show()
        self.visualizzaDottore.pushButton.clicked.connect(self.visualizzaInfoMedicoIndietro)

    def visualizzaInfoMedicoIndietro(self):
        self.visualizzaDottore.close()
        self.menu.show()

