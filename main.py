import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication

from gui.login import Login

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())
