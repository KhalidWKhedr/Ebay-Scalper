# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_databasebMRplk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_form_Database(object):
    def setupUi(self, form_Database):
        if not form_Database.objectName():
            form_Database.setObjectName(u"form_Database")
        form_Database.resize(1039, 661)
        self.frame_MongoDB = QFrame(form_Database)
        self.frame_MongoDB.setObjectName(u"frame_MongoDB")
        self.frame_MongoDB.setGeometry(QRect(190, 200, 441, 241))
        self.frame_MongoDB.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_MongoDB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_MongoDB)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.text_Host = QTextEdit(self.frame_MongoDB)
        self.text_Host.setObjectName(u"text_Host")

        self.gridLayout_2.addWidget(self.text_Host, 1, 1, 1, 1)

        self.label_mongocredentials = QLabel(self.frame_MongoDB)
        self.label_mongocredentials.setObjectName(u"label_mongocredentials")

        self.gridLayout_2.addWidget(self.label_mongocredentials, 0, 1, 1, 1)

        self.label_dbname = QLabel(self.frame_MongoDB)
        self.label_dbname.setObjectName(u"label_dbname")

        self.gridLayout_2.addWidget(self.label_dbname, 6, 0, 1, 1)

        self.text_AuthSource = QTextEdit(self.frame_MongoDB)
        self.text_AuthSource.setObjectName(u"text_AuthSource")

        self.gridLayout_2.addWidget(self.text_AuthSource, 5, 1, 1, 1)

        self.label_port = QLabel(self.frame_MongoDB)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout_2.addWidget(self.label_port, 2, 0, 1, 1)

        self.text_Username = QTextEdit(self.frame_MongoDB)
        self.text_Username.setObjectName(u"text_Username")

        self.gridLayout_2.addWidget(self.text_Username, 3, 1, 1, 1)

        self.text_Port = QTextEdit(self.frame_MongoDB)
        self.text_Port.setObjectName(u"text_Port")

        self.gridLayout_2.addWidget(self.text_Port, 2, 1, 1, 1)

        self.text_DbName = QTextEdit(self.frame_MongoDB)
        self.text_DbName.setObjectName(u"text_DbName")

        self.gridLayout_2.addWidget(self.text_DbName, 6, 1, 1, 1)

        self.label_authsource = QLabel(self.frame_MongoDB)
        self.label_authsource.setObjectName(u"label_authsource")

        self.gridLayout_2.addWidget(self.label_authsource, 5, 0, 1, 1)

        self.label_password = QLabel(self.frame_MongoDB)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout_2.addWidget(self.label_password, 4, 0, 1, 1)

        self.label_username = QLabel(self.frame_MongoDB)
        self.label_username.setObjectName(u"label_username")

        self.gridLayout_2.addWidget(self.label_username, 3, 0, 1, 1)

        self.label_host = QLabel(self.frame_MongoDB)
        self.label_host.setObjectName(u"label_host")

        self.gridLayout_2.addWidget(self.label_host, 1, 0, 1, 1)

        self.text_Password = QTextEdit(self.frame_MongoDB)
        self.text_Password.setObjectName(u"text_Password")

        self.gridLayout_2.addWidget(self.text_Password, 4, 1, 1, 1)

        self.button_Connect = QPushButton(form_Database)
        self.button_Connect.setObjectName(u"button_Connect")
        self.button_Connect.setGeometry(QRect(670, 490, 114, 36))
        self.frame_SSH = QFrame(form_Database)
        self.frame_SSH.setObjectName(u"frame_SSH")
        self.frame_SSH.setGeometry(QRect(190, 20, 441, 181))
        self.frame_SSH.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_SSH.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_SSH)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_SSH_Username = QTextEdit(self.frame_SSH)
        self.text_SSH_Username.setObjectName(u"text_SSH_Username")

        self.gridLayout.addWidget(self.text_SSH_Username, 3, 1, 1, 1)

        self.label_ssh_password = QLabel(self.frame_SSH)
        self.label_ssh_password.setObjectName(u"label_ssh_password")

        self.gridLayout.addWidget(self.label_ssh_password, 4, 0, 1, 1)

        self.label_ssh_host = QLabel(self.frame_SSH)
        self.label_ssh_host.setObjectName(u"label_ssh_host")

        self.gridLayout.addWidget(self.label_ssh_host, 1, 0, 1, 1)

        self.label_ssh_username = QLabel(self.frame_SSH)
        self.label_ssh_username.setObjectName(u"label_ssh_username")

        self.gridLayout.addWidget(self.label_ssh_username, 3, 0, 1, 1)

        self.label_ssh_port = QLabel(self.frame_SSH)
        self.label_ssh_port.setObjectName(u"label_ssh_port")

        self.gridLayout.addWidget(self.label_ssh_port, 2, 0, 1, 1)

        self.label_sshcredentials = QLabel(self.frame_SSH)
        self.label_sshcredentials.setObjectName(u"label_sshcredentials")

        self.gridLayout.addWidget(self.label_sshcredentials, 0, 1, 1, 1)

        self.checkbox_SSH = QCheckBox(self.frame_SSH)
        self.checkbox_SSH.setObjectName(u"checkbox_SSH")

        self.gridLayout.addWidget(self.checkbox_SSH, 0, 0, 1, 1)

        self.text_SSH_Host = QTextEdit(self.frame_SSH)
        self.text_SSH_Host.setObjectName(u"text_SSH_Host")

        self.gridLayout.addWidget(self.text_SSH_Host, 1, 1, 1, 1)

        self.text_SSH_Password = QTextEdit(self.frame_SSH)
        self.text_SSH_Password.setObjectName(u"text_SSH_Password")

        self.gridLayout.addWidget(self.text_SSH_Password, 4, 1, 1, 1)

        self.text_SSH_Port = QTextEdit(self.frame_SSH)
        self.text_SSH_Port.setObjectName(u"text_SSH_Port")

        self.gridLayout.addWidget(self.text_SSH_Port, 2, 1, 1, 1)

        self.frame_auth = QFrame(form_Database)
        self.frame_auth.setObjectName(u"frame_auth")
        self.frame_auth.setGeometry(QRect(630, 20, 219, 234))
        self.frame_auth.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_auth.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_auth)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radio_AWS = QRadioButton(self.frame_auth)
        self.radio_AWS.setObjectName(u"radio_AWS")

        self.gridLayout_3.addWidget(self.radio_AWS, 5, 0, 1, 1)

        self.radio_X509 = QRadioButton(self.frame_auth)
        self.radio_X509.setObjectName(u"radio_X509")

        self.gridLayout_3.addWidget(self.radio_X509, 4, 0, 1, 1)

        self.radio_KERBEROS = QRadioButton(self.frame_auth)
        self.radio_KERBEROS.setObjectName(u"radio_KERBEROS")

        self.gridLayout_3.addWidget(self.radio_KERBEROS, 6, 0, 1, 1)

        self.radio_SHA256 = QRadioButton(self.frame_auth)
        self.radio_SHA256.setObjectName(u"radio_SHA256")

        self.gridLayout_3.addWidget(self.radio_SHA256, 2, 0, 1, 1)

        self.radio_LDAP = QRadioButton(self.frame_auth)
        self.radio_LDAP.setObjectName(u"radio_LDAP")

        self.gridLayout_3.addWidget(self.radio_LDAP, 3, 0, 1, 1)

        self.r = QRadioButton(self.frame_auth)
        self.r.setObjectName(u"r")

        self.gridLayout_3.addWidget(self.r, 7, 0, 1, 1)

        self.radio_SHA1 = QRadioButton(self.frame_auth)
        self.radio_SHA1.setObjectName(u"radio_SHA1")

        self.gridLayout_3.addWidget(self.radio_SHA1, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_auth)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.button_TestConnection = QPushButton(form_Database)
        self.button_TestConnection.setObjectName(u"button_TestConnection")
        self.button_TestConnection.setGeometry(QRect(160, 460, 161, 36))

        self.retranslateUi(form_Database)

        QMetaObject.connectSlotsByName(form_Database)
    # setupUi

    def retranslateUi(self, form_Database):
        form_Database.setWindowTitle(QCoreApplication.translate("form_Database", u"Database Configuration Settings", None))
        self.label_mongocredentials.setText(QCoreApplication.translate("form_Database", u"MongoDB Credentials:", None))
        self.label_dbname.setText(QCoreApplication.translate("form_Database", u"DB NAME:", None))
        self.label_port.setText(QCoreApplication.translate("form_Database", u"PORT:", None))
        self.label_authsource.setText(QCoreApplication.translate("form_Database", u"AUTH SOURCE:", None))
        self.label_password.setText(QCoreApplication.translate("form_Database", u"PASSWORD:", None))
        self.label_username.setText(QCoreApplication.translate("form_Database", u"USERNAME:", None))
        self.label_host.setText(QCoreApplication.translate("form_Database", u"HOST:", None))
        self.button_Connect.setText(QCoreApplication.translate("form_Database", u"Connect", None))
        self.label_ssh_password.setText(QCoreApplication.translate("form_Database", u"SSH PASSWORD:", None))
        self.label_ssh_host.setText(QCoreApplication.translate("form_Database", u"SSH HOST:", None))
        self.label_ssh_username.setText(QCoreApplication.translate("form_Database", u"SSH USERNAME:", None))
        self.label_ssh_port.setText(QCoreApplication.translate("form_Database", u"SSH PORT:", None))
        self.label_sshcredentials.setText(QCoreApplication.translate("form_Database", u"SSH Credentials", None))
        self.checkbox_SSH.setText(QCoreApplication.translate("form_Database", u"SSH", None))
        self.radio_AWS.setText(QCoreApplication.translate("form_Database", u"MO&NGODB-AWS  ", None))
        self.radio_X509.setText(QCoreApplication.translate("form_Database", u"MONGODB-&X509  ", None))
        self.radio_KERBEROS.setText(QCoreApplication.translate("form_Database", u"&GSSAPI (Kerberos)  ", None))
        self.radio_SHA256.setText(QCoreApplication.translate("form_Database", u"SCRAM-SHA-&256  ", None))
        self.radio_LDAP.setText(QCoreApplication.translate("form_Database", u"L&DAP", None))
        self.r.setText(QCoreApplication.translate("form_Database", u"P&LAIN  ", None))
        self.radio_SHA1.setText(QCoreApplication.translate("form_Database", u"SCRAM-SHA-&1  ", None))
        self.label_6.setText(QCoreApplication.translate("form_Database", u"Authentication Types:", None))
        self.button_TestConnection.setText(QCoreApplication.translate("form_Database", u"Test Connection", None))
    # retranslateUi

