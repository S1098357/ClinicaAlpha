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
        self.richiediPagamentoGUI=None
        self.RUDClienteGUI=None
        self.sceltaClienteGUI=None
        self.clienteScelto=Cliente()
        self.CCScelta=CartellaClinica()
        self.modificaClienteGUI=None
        self.appoggioNome=''
        self.visualizzaClienteGUI=None
        self.MessaggioGUI=None
        self.ricevuta=Ricevuta()
        self.ricevutaGUI=None
        self.modificaOraroDottoreGUI=None

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
        self.menu.hide()
        self.menuStampaGUI=MenuStampaGUI()
        self.menuStampaGUI.show()
        self.menuStampaGUI.pushButton.clicked.connect(self.stampaRicetta)
        self.menuStampaGUI.pushButton_2.clicked.connect(self.stampaCertificato)
        self.menuStampaGUI.pushButton_3.clicked.connect(self.chiudiTutto)

    def stampaRicetta(self):
        self.menuStampaGUI.hide()
        if self.segreteria.leggiRicetta!=False:
            self.ricetta=self.segreteria.leggiRicetta()
            self.stampaRicettaGUI = VisualizzaRicettaGUI(self.ricetta)
            self.stampaRicettaGUI.show()
            self.stampaRicettaGUI.pushButton.clicked.connect(self.chiudiTutto)
        else:
            self.chiudiTutto()

    def stampaCertificato(self):
        self.menuStampaGUI.hide()
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

    def richiediPagamento(self):
        self.menu.hide()
        if self.segreteria.leggiCertificato != False:
            self.certificato=self.segreteria.leggiCertificato
            self.richiediPagamentoGUI=self.richiediPagamentoGUI(self.certificato.prezzo)
            self.richiediPagamentoGUI.show()
            self.richiediPagamentoGUI.pushButton.clicked.connect(self.self.emettiRicevuta)
            self.richiediPagamentoGUI.pushButton_2.clicked.connect(self.chiudiTutto)
        else:
            self.chiudiTutto()

    def emettiRicevuta(self):
        self.ricevuta.prezzo=self.certificato.prezzo
        self.richiediPagamentoGUI.close()
        self.ricevuta.salva()
        self.ricevutaGUI=RicevutaGUI(self.ricevuta)
        self.ricevutaGUI.show()
        self.ricevutaGUI.pushButton.clicked.connect(self.chiudiTutto)

    def RUDCliente(self):
        self.menu.hide()
        self.RUDClienteGUI=RUDClienteGUI()
        self.RUDClienteGUI.show()
        self.RUDClienteGUI.pushButton.clicked.connect(self.modificaCliente)
        self.RUDClienteGUI.pushButton_2.clicked.connect(self.visualizzaCliente)
        self.RUDClienteGUI.pushButton_3.clicked.connect(self.eliminaCliente)
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
        self.visualizzaClienteGUI=VisualizzaClienteGUI(self.clienteScelto)
        self.visualizzaClienteGUI.show()
        self.visualizzaClienteGUI.pushButton.clicked.connect(self.chiudiTutto)

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
        for cliente in self.listaClienti:
            if self.clienteScelto.nomeCognome==cliente.nomeCognome:
                self.listaClienti.remove(cliente)
        self.segreteria.listaClienti = self.listaClienti
        self.segreteria.salvaClienti()
        self.menu.show()

    def scriviMessaggio(self):
        self.menu.hide()
        self.RUDClienteGUI.close()
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
            self.clienteScelto.messaggio.append(self.MessaggioGUI.textEdit.toPlainText())
            self.clienteScelto.salvaMessaggio()
        else:
            for cliente in self.listaClienti:
                cliente.messaggio.append(self.MessaggioGUI.textEdit.toPlainText())
                self.clienteScelto.salvaMessaggio()

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
        data,giornoSett=self.modificaOraroDottoreGUI.currentText().split(' ')
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
        self.menu.show()
















