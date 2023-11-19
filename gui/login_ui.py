# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import imagenes_rc

class Ui_formLogin(object):
    def setupUi(self, formLogin):
        if not formLogin.objectName():
            formLogin.setObjectName(u"formLogin")
        formLogin.setWindowModality(Qt.NonModal)
        formLogin.setEnabled(True)
        formLogin.resize(370, 339)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formLogin.sizePolicy().hasHeightForWidth())
        formLogin.setSizePolicy(sizePolicy)
        formLogin.setMinimumSize(QSize(370, 339))
        formLogin.setMaximumSize(QSize(370, 339))
        formLogin.setAutoFillBackground(False)
        formLogin.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black")
        formLogin.setSizeGripEnabled(True)
        formLogin.setModal(True)
        self.label = QLabel(formLogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 311, 91))
        self.label.setPixmap(QPixmap(u":/xy/logo_banco.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(formLogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 110, 131, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"")
        self.label_2.setInputMethodHints(Qt.ImhNone)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_3 = QLabel(formLogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(27, 154, 91, 21))
        self.label_3.setFont(font)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_4 = QLabel(formLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 202, 91, 21))
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.RichText)
        self.txtUsuario = QLineEdit(formLogin)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(140, 150, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Emoji"])
        self.txtUsuario.setFont(font1)
        self.txtUsuario.setStyleSheet(u"")
        self.txtClave = QLineEdit(formLogin)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setGeometry(QRect(140, 198, 181, 31))
        self.txtClave.setFrame(True)
        self.txtClave.setEchoMode(QLineEdit.Password)
        self.btnAcceder = QPushButton(formLogin)
        self.btnAcceder.setObjectName(u"btnAcceder")
        self.btnAcceder.setGeometry(QRect(120, 250, 111, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.btnAcceder.setFont(font2)
        self.btnAcceder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAcceder.setStyleSheet(u"background-color: rgb(37, 116, 204);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.btnAcceder.setCheckable(False)
        self.btnAcceder.setFlat(False)
        self.lblMensaje = QLabel(formLogin)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setGeometry(QRect(40, 300, 281, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        self.lblMensaje.setFont(font3)
        self.lblMensaje.setStyleSheet(u"color: rgb(179, 24, 74);")
        self.lblMensaje.setAlignment(Qt.AlignCenter)

        self.retranslateUi(formLogin)

        QMetaObject.connectSlotsByName(formLogin)
    # setupUi

    def retranslateUi(self, formLogin):
        formLogin.setWindowTitle(QCoreApplication.translate("formLogin", u"Inicio de sesi\u00f3n", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("formLogin", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Inicio de sesi\u00f3n</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("formLogin", u"<html><head/><body><p align=\"right\">Usuario</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("formLogin", u"<html><head/><body><p align=\"right\">Contrase\u00f1a</p></body></html>", None))
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("formLogin", u"Ingresar usuario", None))
        self.txtClave.setPlaceholderText(QCoreApplication.translate("formLogin", u"Ingresar contrase\u00f1a", None))
        self.btnAcceder.setText(QCoreApplication.translate("formLogin", u"Acceder", None))
        self.lblMensaje.setText(QCoreApplication.translate("formLogin", u"mensaje", None))
    # retranslateUi

