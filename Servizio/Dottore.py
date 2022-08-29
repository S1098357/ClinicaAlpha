import datetime

#from Amministrazione.Segreteria import Segreteria
import os.path

from Servizio.CertificatoMalattia import CertificatoMalattia
from Servizio.CertificatoMedicoAgonistico import CertificatoMedicoAgonistico
from Servizio.CertificatoSanaRobustaCostituzione import CertificatoSanaRobustaCostituzione
from Servizio.Cliente import Cliente
from Servizio.Ricetta import Ricetta
import pickle


class Dottore:

    def __init__(self,nomeCognome,numTelefono):
        self.documento = None
        self.clienteAttuale=Cliente()
        self.listaPrenotazioniOggi=[]
        self.nomeCognome=nomeCognome
        self.numeroDiTelefono=numTelefono
        self.OrarioLavoro=[datetime.time(10),datetime.time(10),datetime.time(10),datetime.time(10),datetime.time(10)]
        self.listaCartelleCliniche=[]
        self.modificheOrario=[]

    def ricercaCartellaClinica(self,id):
        for CC in self.listaCartelleCliniche:
            if CC.GetId==id:
                return CC

    def aggiornaCartellaClinica(self):
        CC=self.ricercaCartellaClinica(self.ClienteAttuale.id)
        appoggio=(AggiornaCCGUI(CC.patologie))
        if appoggio!=None:
            CC.setPatologie(appoggio)
            CC.stampaCartella()

    def chiamaClienteSuccessivo(self):
        for prenotazione in self.listaPrenotazioniOggi:
            if prenotazione.nomeCliente==self.clienteAttuale.nomeCognome:
                prenAttuale=prenotazione
                if prenotazione==self.listaPrenotazioniOggi[len(self.listaPrenotazioniOggi)-1]:
                    self.clienteAttuale=None
                else:
                    appoggio=self.listaPrenotazioniOggi[self.listaPrenotazioniOggi.index(prenotazione)+1]
                    self.ClienteAttuale=self.ricercaCliente(appoggio.nomeCliente)
        self.listaPrenotazioniOggi.remove(prenAttuale)

    def ricercaCliente(self,cliente):
        for elem in self.listaClienti:
            if elem.nomeCognome==cliente:
                return elem

    #def compilaCertificato(self):
     #   tipo=grafica.tipoCertificato()
     #   if tipo=='certificato di malattia':
      #      self.documento=CertificatoMalattia()
       # else:
        #    if tipo=='certificato sana e robusta costituzione'
         #       self.documento=CertificatoSanaERobustaCostituzione()
          #  else:
           #     self.documento=CertificatoAgoistico()
        #self.certificatoMedico.compilaCertificato(self.nomeCognome, self.clienteAttuale.nomeCognome, datetime.now())

    #def prescriviFarmaco(self):
        #self.documento.compilaRicetta(self.clienteAttuale.nomeCognome,self.nomeCognome,datetime.now(),grafica.compilaRicetta())

    #def setDataOraLavoro(self):
       # self.orarioLavoro.append(grafica.scegliOrario())

    def visualizzaCartellaClienteAttuale(self):
        CC=self.ricercaCartellaClinica(self.ClienteAttuale.id)
        VisualizzaCCGUI(CC.patologie)

    def visualizzaPrenotazioni(self):
        VisualizzaTuttePrenotazioniGUI(self.listaPrenotazioniOggi)

    def ricercaPrenotazioneOggi(self,listaPrenotazioni):
        for prenotazione in listaPrenotazioni:
            if prenotazione.dataOra.day==datetime.today().day:
                self.listaPrenotazioniOggi.append(prenotazione)


    def menuDottore(self):
        risposta=MenuDottoreGUI(self.clienteAttuale.nomeCognome)
        while True:
            match risposta:
                case 0:
                    cliente,tipo,prezzo=CompilaCertificatoGUI(self.clienteAttuale,self.nomeCognome)
                    match tipo:
                        case 'certificato agonistico':
                            self.documento=CertificatoMedicoAgonistico()
                        case 'certificato malattia':
                            self.documento=CertificatoMalattia()
                        case 'sana e robusta costituzione':
                            self.documento=CertificatoSanaRobustaCostituzione()
                    if self.documento!=None:
                        self.documento.compilaCertificato(cliente,self.nomeCognome,datetime.today())
                        self.documento.stampa()
                case 1:
                    cliente,farmacoPrescritto=CompilaRicettaGUI(self.nomeCognome,self.clienteAttuale)
                    if cliente!=None and farmacoPrescritto!=None:
                        self.documento=Ricetta()
                        self.documento.compilaRicetta(farmacoPrescritto,cliente,self.nomeCognome,datetime.today())
                        self.documento.stampa()
                case 3:
                    self.chiamaClienteSuccessivo()
                    self.menuDottore()
                case 5:
                    self.visualizzaPrenotazioni()
                case 2:
                    self.aggiornaCartellaClinica()
                case 4:
                    self.visualizzaCartellaClienteAttuale()

    def dottorePre(self,listaPrenotazioni,listaClienti):
        self.ricercaPrenotazioneOggi(listaPrenotazioni)
        if self.listaPrenotazioniOggi!=None:
            for cliente in listaClienti:
                if cliente.nomeCognome==self.listaPrenotazioniOggi[0].nomeCliente:
                    self.clienteAttuale=cliente
            self.menuDottore()
        else:
            self.clienteAttuale=None

    def salvaOrari(self,orario):
        modifiche=[]
        if os.path.isfile('dati/Orari' + self.nomeCognome + '.pickle'):
            with open('dati/Orari' + self.nomeCognome + '.pickle', 'rb+') as f:
                modifiche=pickle.load(f)
                modifiche.append(orario)
            with open ('dati/Orari'+self.nomeCognome+'.pickle','wb+') as f:
                pickle.dump(modifiche,f)
        else:
            modifiche.append(orario)
            with open ('dati/Orari'+self.nomeCognome+'.pickle' , 'wb+') as f:
                pickle.dump(modifiche,f,pickle.HIGHEST_PROTOCOL)

    def leggiOrari(self):
        import datetime

        if os.path.isfile('dati/Orari'+self.nomeCognome+'.pickle'):
            with open('dati/Orari'+self.nomeCognome+'.pickle', 'rb+') as f:
                self.modificheOrario = pickle.load(f)
            for modifica in self.modificheOrario:
                app , giornoSett , orario = modifica.split(' ')
                data=datetime.datetime.strptime(app,'%m/%d/%Y').date()
                if data<datetime.datetime.now().date():
                    self.modificheOrario.remove(modifica)
                else:
                    diff = data - datetime.datetime.now().date()
                    if data.weekday()>datetime.datetime.now().weekday():
                        posto=diff.days
                    else:
                        posto=diff.days-2
                    match orario:
                        case '9.00':
                            self.OrarioLavoro[posto]=datetime.time(9)
                        case '10.00':
                            self.OrarioLavoro[posto] =datetime.time(10)
                        case '11.00':
                            self.OrarioLavoro[posto] = datetime.time(11)
                        case '12.00':
                            self.OrarioLavoro[posto] = datetime.time(12)
            self.sovrascriviOrari(self.modificheOrario)
            return True
        else:
            return False

    def sovrascriviOrari(self,orari):
        with open('dati/Orari' + self.nomeCognome + '.pickle', 'wb+') as f:
            pickle.dump(orari, f, pickle.HIGHEST_PROTOCOL)