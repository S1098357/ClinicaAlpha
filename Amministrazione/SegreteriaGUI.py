class SegreteriaGUI:

    def __init__(self):
        self.segreteria=Segreteria()
        self.segreteria.leggiClienti()
        self.listaClienti=self.segreteria.listaClienti
        self.caledario=Calendario()
        self.sistema=Sistema(self.calendario.Dottori)
        self.sistema.leggiPrenotazioni()
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
        self.certificato=Certificato()
        self.stampaCertificatoGUI=None

    def Menu(self):
        self.menu.show()
        self.menu.pushButton.clicked.connect(self.eliminaCC)
        self.menu.pushButton_2.clicked.connect(self.stampaDocumenti)
        self.menu.pushButton_3.clicked.connect(self.visualizzaEliminaPren)
        self.menu.pushButton_4.clicked.connect(self.RUDCliente)
        self.menu.pushButton_5.clicked.connect(self.visualizzaStanze)
        self.menu.pushButton_6.clicked.connect(self.inviaMessaggio)
        self.menu.pushButton_7.clicked.connect(self.richiediPagamento)
        self.menu.pushButton_8.clicked.connect(self.modificaOrarioDottore)

    def chiudiTutto(self):
        pass

    def eliminaCC(self):
        self.menu.hide()
        self.eliminaCCGUI=EliminaCCGUI(self.listaId)
        self.eliminaCCGUI.show()
        self.eliminaCCGUI.pushButton.clicked.connect(self.rimuoviCC)
        self.eliminaCCGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def rimuoviCC(self):
        self.eliminaCCGUI.close()
        self.segreteria.eliminaCartellaClinica(eliminaCCGUI.comboBox.currentText())
        self.menu.show()

    def stampaDocumenti(self):
        self.menuStampaGUI=MenuStampaGUI()
        self.menuStampaGUI.show()
        self.menuStampaGUI.pushButton.clicked.connect(self.stampaRicetta)
        self.menuStampaGUI.pushButton_2.clicked.connect(self.stampaCertificato)
        self.menuStampaGUI.pushButton_3.clicked.connect(self.chiudiTutto)

    def stampaRicetta(self):
        if self.segreteria.leggiRicetta!=False:
            self.ricetta=self.segreteria.leggiRicetta()
            self.stampaRicettaGUI = VisualizzaRicettaGUI(self.ricetta)
            self.stampaRicettaGUI.show()
            self.stampaRicettaGUI.pushButton.clicked.connect(self.chiudiTutto)
        else:
            self.chiudiTutto()

    def stampaCertificato(self):
        if self.segreteria.leggiCertificato != False:
            self.certificato=self.segreteria.leggiCertificato
            self.stampaCertificatoGUI=VisualizzaCertificatoGUI(self.certificato)
            if self.certificato.prezzo==50.00:
                self.stampaCertificatoGUI.textBrowser.setText('Si attesta l''idoneità fisica del paziente allo sport agonistico')
            if self.certificato.prezzo==0:
                self.stampaCertificatoGUI.textBrowser.setText('Si attesta lo stato di malattia del paziente')
            else:
                self.stampaCertificatoGUI.textBrowser.setText('Si attesta lo stato di buona salute del paziente')
                self.stampaCertificatoGUI.pushButton.clicked.connect(self.chiudiTutto)
        else:
            self.chiudiTutto()

    def visualizzaEliminaPren(self):
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
            lista.append(prenotazione.cliente+' : '+ prenotazione.dataOra.strftime('%y-%m-%d %H:%M'))
        self.eliminaPrenGUI=EliminaPrenotazioneGUI(lista)
        self.eliminaPrenGUI.show()
        self.eliminaPrenGUI.pushButton.clicked.connect(self.rimuoviPren)
        self.eliminaPrenGUI.pushButton_2.clicked.connect(self.chiudiTutto)

    def rimuoviPren(self):
        appoggio=self.eliminaPrenGUI.comboBox.currentText()
        self.eliminaPrenGUI.close()
        appoggio=appoggio[':']
        appoggio=appoggio[' ']
        for prenotazione in self.sistema.listaPrenotazioni:
            if prenotazione.dataOra==datetime.strptime(appoggio,'%y-%m-%d %H:%M'):
                sistema.listaPrenotazioni.remove(prenotazione)
        self.sistema.salvaPrenotazioni()
        self.menu.show()







