import sys

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton

import gui.imagenes_rc


class Login(QMainWindow):
    # Constructor y controla la visualización del Widget
    def __init__(self):
        super(Login, self).__init__()
        ui_file_name = "gui/login.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.OpenModeFlag.ReadOnly):
            print(f'Cannot open {ui_file_name}: {ui_file.errorString()}')
            sys.exit(-1)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)

        self.setCentralWidget(self.ui)

        self.ui.findChild(QLabel, 'lblMensaje').setText('')
        self.initGUI()

    # Validaciones
    def ingresar(self):
        self.ui.findChild(QLabel, 'lblMensaje').setText('')
        txtUsuario: QLineEdit = self.ui.findChild(QLineEdit, 'txtUsuario')
        txtClave: QLineEdit = self.ui.findChild(QLineEdit, 'txtClave')
        lblMensaje: QLabel = self.ui.findChild(QLabel, 'lblMensaje')
        if txtUsuario.text() == '' and txtClave.text() == '':
            lblMensaje.setText(
                'Ingrese un usuario y contraseña válidos')
            txtUsuario.setFocus()
        elif len(txtUsuario.text()) < 2:
            lblMensaje.setText(
                'Ingrese un usuario válido')
            txtUsuario.setFocus()
        elif len(txtClave.text()) < 3:
            lblMensaje.setText(
                'Ingrese una contraseña válida')
            txtClave.setFocus()
        else:
            lblMensaje.setText(
                'Pasó')
            pass

    # Al pulsar Acceder
    def initGUI(self):
        btnAcceder: QPushButton = self.ui.findChild(
            QPushButton, 'btnAcceder')
        btnAcceder.clicked.connect(self.ingresar)
