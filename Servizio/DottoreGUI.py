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
        self.menu=MenuDottoreGUI()
        self.prenotazioneAttuale=None

    def setUp(self):
        for prenotazione in sistema.listaPrenotazioni:
            if prenotazione.dataOra.date==datetime.datetime.today() and prenotazione.dottore==self.nomeCognome:
                self.listaPrenotazioniOggi.append(prenotazione)
        self.listaPrenotazioniOggi=sorted(self.listaPrenotazioniOggi)
        self.clienteAttuale=self.listaPrenotazioniOggi[0].cliente
        self.prenotazioneAttuale=self.listaPrenotazioniOggi[0]
        self.menu.label = 'Cliente attuale:' + self.clienteAttuale
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
        if self.clienteAttuale!=None:
            self.menu.label='Cliente attuale:' + self.clienteAttuale
        else:
            self.menu.label = 'Non ci sono altri appuntamenti'
        #self.menu.show()

