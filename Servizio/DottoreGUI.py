import datetime

class DottoreGUI:

    def __init__(self,dottore):
        self.documento = dottore.documento
        self.clienteAttuale = Cliente()
        self.listaPrenotazioniOggi = dottore.listaPrenotazioniOggi
        self.nomeCognome = dottore.nomeCognome
        self.numeroDiTelefono = dottore.numTelefono
        self.OrarioLavoro = dottore.OrarioLavoro
        self.listaCartelleCliniche = dottore.listaCartelleCliniche
        self.sistema=Sistema()
        self.menu=None
        self.prenotazioneAttuale=None
        self.ricetta=Ricetta()
        self.ricettaGUI=None
        self.CC=CartellaClinica()
        self.AggiornaCC=None
        self.VisualizzaCC=None

    def setUp(self):
        for prenotazione in sistema.listaPrenotazioni:
            if prenotazione.dataOra.date==datetime.datetime.today() and prenotazione.dottore==self.nomeCognome:
                self.listaPrenotazioniOggi.append(prenotazione)
        self.listaPrenotazioniOggi=sorted(self.listaPrenotazioniOggi)
        self.clienteAttuale=self.listaPrenotazioniOggi[0].cliente
        self.prenotazioneAttuale=self.listaPrenotazioniOggi[0]
        self.menu.label = 'Cliente attuale:' + self.clienteAttuale.nomeCognome
        self.menu.show()
        self.menu.pushButton.clicked.connect(self.compilaCertificato)
        self.menu.pushButton_2.clicked.connect(self.compilaRicetta)
        self.menu.pushButton_3.clicked.connect(self.aggiornaCC)
        self.menu.pushButton_4.clicked.connect(self.chiamaClienteSucc)
        self.menu.pushButton_5.clicked.connect(self.visualizzaListaAppuntamenti)
        self.menu.pushButton_6.clicked.connect(self.visualizzaCC)

    def chiamaClienteSucc(self):
        #self.menu.hide()
        for prenotazione in self.listaPrenotazioniOggi:
            if prenotazione==self.prenotazioneAttuale:
                if self.listaPrenotazioniOggi[self.prenotazioneAttuale.index()+1]!=None:
                    self.prenotazioneAttuale=self.listaPrenotazioniOggi[self.prenotazioneAttuale.index()+1]
                    self.clienteAttuale=self.prenotazioneAttuale.cliente
                else:
                    self.prenotazioneAttuale = None
                    self.clienteAttuale = None
        self.menu=MenuDottoreGUI(self.clienteAttuale.nomeCognome)
        #self.menu.show()

    def compilaRicetta(self):
        #self.menu.hide()
        self.ricettaGUI=CompilaRicettaGUI(self.clienteAttuale,self.nomeCognome)
        self.ricettaGUI.show()
        self.ricettaGUI.pushButton.clicked.connect(self.inviaRicettaSegreteria)
        self.ricettaGUI.pushButton_2.clicked.connect(self.menu.show)

    def inviaRicettaSegreteria(self):
        self.ricetta.farmacoPrescritto=self.ricettaGUI.textEdit.text()
        self.ricetta.stampaRicetta()
        self.menu.show()

    def aggiornaCC(self):
        self.CC.id=self.clienteAttuale.id
        self.CC.patologie=self.CC.leggiCartella()
        self.AggiornaCC=AggiornaCCGUI(self.CC.patologie)
        self.AggiornaCC.show()
        self.pushButton.clicked.connect(self.modificaCartella)

    def modificaCartela(self):
        self.CC.patologie=self.AggiornaCC.textEdit.text()
        self.CC.stampaCartella()
        self.menu.show()

    def visualizzaCC(self):
        self.CC.id = self.clienteAttuale.id
        self.CC.patologie = self.CC.leggiCartella()
        self.VisualizzaCC=VisualizzaCCGUI(self.CC.patologie,self.clienteAttuale.nomeCognome)
        self.VisualizzaCC.show()
        self.VisualizzaCC.pushButton.clicked.connect(self.menu.show)

