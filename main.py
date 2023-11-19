import sys
from PySide6.QtWidgets import QApplication
from gui.login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
