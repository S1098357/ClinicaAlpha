import sys

from PyQt5.QtWidgets import QApplication

from GUI.LoginGUI import LoginGUI


class main:
    app = QApplication(sys.argv)
    login = LoginGUI()
    login.login()
    sys.exit(app.exec_())