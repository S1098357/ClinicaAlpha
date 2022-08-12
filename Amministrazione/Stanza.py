import datetime



class Stanza:

    def __init__(self, dottore, numeroDiStanza):
        self.numeroDiStanza = numeroDiStanza
        self.orarioLibero = datetime.datetime (2000,3,10)
        self.occupata = False
        self.dottore = dottore

    def getOccupata(self):
        return self.occupata

    def setOccupata(self, occupata):
        self.occupata = occupata

