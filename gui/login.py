import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton

import gui.imagenes_rc


class Login():
    # Constructor y controla la visualización del Widget
    def __init__(self):
        self.ui_file_name = "gui/login.ui"
        self.ui_file = QFile(self.ui_file_name)
        if not self.ui_file.open(QIODevice.OpenModeFlag.ReadOnly):
            print(f'Cannot open {self.ui_file_name}: {
                  self.ui_file.errorString()}')
            sys.exit(-1)
        self.loader = QUiLoader()
        self.window = self.loader.load(self.ui_file)
        self.ui_file.close()
        if not self.window:
            print(self.loader.errorString())
            sys.exit(-1)

        self.window.findChild(QLabel, 'lblMensaje').setText('')
        self.initGUI()
        self.window.show()

    # Validaciones
    def ingresar(self):
        self.window.findChild(QLabel, 'lblMensaje').setText('')
        txtUsuario: QLineEdit = self.window.findChild(QLineEdit, 'txtUsuario')
        txtClave: QLineEdit = self.window.findChild(QLineEdit, 'txtClave')
        lblMensaje: QLabel = self.window.findChild(QLabel, 'lblMensaje')
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
        btnAcceder: QPushButton = self.window.findChild(
            QPushButton, 'btnAcceder')
        btnAcceder.clicked.connect(self.ingresar)
