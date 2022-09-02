import os.path
import pickle
from unittest import TestCase

#from Servizio.Dottore import Dottore


class TestModificaOrarioDottore(TestCase):

    def testModificaOrarioDottore(self):
        self.dottore=Dottore('prova',123)
        prova='9/2/2022 venerdì 9.00'
        dottore.salvaOrari('9/2/2022 venerdì 9.00')
        orari=None
        if os.path.isfile('Dati/Orariprova.pickle'):
            with open('Dati/Orariprova.pickle', 'rb+') as f:
                orari=pickle.load(f)
        self.assertIsNotNone(orari)
        for orario in orari:
            self.assertEqual(orario,prova)
