from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class UltimoMessaggioGUI(QDialog):

    def __init__(self,messaggio):
        super(UltimoMessaggioGUI, self).__init__()
        loadUi("GUI/UltimoMessaggioGUI.ui", self)
        messaggi=''
        i=0
        for msg in messaggio:
            i+=1
            messaggi=messaggi+'\n'+str(i)+'° messaggio : '+msg
        self.label_2.setText(messaggi)