class RichiediPagamentoGUI:

    def __init__(self,prezzo):
        super(RichiediPagamentoGUI, self).__init__()
        loadUi("GUI/RichiediPagamentoGUI.ui", self)
        self.label.setText('Prezzo : ' + prezzo)