from Servizio.CertificatoMedico import CertificatoMedico


class CertificatoMalattia(CertificatoMedico):

    def __init__(self):
        super().__init__()
        self.prezzo=0.00

    def compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio):
        super().compilaCertificato(nomePaziente,nomeCognomeDottore,dataRilascio)

    def stampaCertificato(self):
        super().stampaCertificato()