import datetime
import pickle

from GUI.LeggiRicevutaGUI import LeggiRicevutaGUI


class Ricevuta():

    def __init__(self):
        self.prezzo=0
        self.dataRilascio=datetime.date

    def salva(self,prezzo):
        self.prezzo=prezzo
        self.dataRilascio=datetime.date.today()
        #dizio={
        #    'importo:':self.prezzo,
        #    'data rilascio:':self.dataRilascio
        #}
        with open ('dati/Ricevuta.pickle' , 'wb+') as f:
            pickle.dump(self,f,pickle.HIGHEST_PROTOCOL)

    def stampa(self):
        if open('dati/Ricevuta.pickle', 'rb') :
            with open('dati/Ricevuta.pickle', 'rb') as f:
                return pickle.load(f)
        else:
            return False
