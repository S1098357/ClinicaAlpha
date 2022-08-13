from Servizio.CertificatoMedico import CertificatoMedico


class CertificatoMedicoAgonistico(CertificatoMedico):

    def __init__(self):
        super().__init__()
        self.prezzo=50.00

    def compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio):
        super().compilaCertificato(nomePaziente,nomeCognomeDottore,dataRilascio)

    def stampaCertificato(self):
        super().stampaCertificato()