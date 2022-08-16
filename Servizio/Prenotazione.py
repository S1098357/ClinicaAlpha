import datetime

class Prenotazione:

    def __init__(self):
        self.certificatoMedico=False
        self.cliente=None
        self.dataOra=datetime.datetime
        self.dottore=None
        self.durataVisita=datetime.time(0,15)
        self.note=None
        self.ricettaMedica=False
        self.visitaGenerica=False


    def setCliente(self,cliente):
        self.cliente=cliente

    def setDottore(self,dottore):
        self.dottore=dottore

    def setDataOra(self,dataOra):
        self.dataOra=dataOra

    def setNote(self,note):
        self.note=note

    def setTipoAppuntamento(self):
        pass

    def getDataOra(self):
        return self.dataOra

    def getCliente(self):
        return self.cliente

    def getDottore(self):
        return self.dottore

    def getTipoAppuntamento(self):
        #return self.tipoAppuntamento
        pass

    def stampaPrenotazione(self):
        return {
            'Certificato Medico': self.certificatoMedico,
            'Cliente' : self.cliente,
            'Data ed Ora': self.dataOra,
            'Dottore' : self.dottore,
            'Durata della Visita': self.durataVisita,
            'Note':self.note,
            'Ricetta Medica':self.ricettaMedica,
            'Visita Generica':self.visitaGenerica
        }