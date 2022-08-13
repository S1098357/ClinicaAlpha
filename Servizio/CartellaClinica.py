import os
import pickle


class CartellaClinica:


    def __init__(self, id):
        self.id=id
        self.patologie=''

    def stampaCartella(self):
        dizio={'patologie': self.patologie}
        #if os.path.isfile ('dati/CC/cartella'+str(self.id)+'.pickle'):
        with open ('dati/CC/cartella'+str(self.id)+'.pickle' , 'wb+') as f:
            pickle.dump(dizio,f,pickle.HIGHEST_PROTOCOL)
        #else:
            #print ('c')

    def leggiCartella(self):
        if os.path.isfile('dati/CC/cartella'+str(self.id)+'.pickle'):
            with open('dati/CC/cartella'+str(self.id)+'.pickle', 'rb') as f:
                return pickle.load(f)
        else:
            return False