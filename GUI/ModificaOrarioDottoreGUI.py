import datetime

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import datetime

class ModificaOrarioDottoreGUI(QDialog):

    def __init__(self,listaDottori):
        super(ModificaOrarioDottoreGUI, self).__init__()
        loadUi("GUI/ModificaOrarioDottoreGUI.ui", self)
        self.comboBox.addItems(listaDottori)
        data=datetime.datetime.now().date()
        lista=[]
        appoggio=''
        for i in range (0,6):
            data=data+datetime.timedelta(days=1)
            match data.weekday():
                case 0:
                    appoggio='lunedì'
                case 1:
                    appoggio='martedì'
                case 2:
                    appoggio='mercoledì'
                case 3:
                    appoggio='giovedì'
                case 4:
                    appoggio='venerdì'
                case 5:
                    appoggio='festivo'
                case 6:
                    appoggio='festivo'
            if appoggio!='festivo':
                lista.append(data.strftime('%m/%d/%Y')+' '+appoggio)
        self.comboBox_2.addItems(lista)
        self.comboBox_3.addItems(['9.00','10.00','11.00','12.00'])

