# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_databasePvpExj.ui'
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
    QGridLayout, QLabel, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

class Ui_form_Database(object):
    def setupUi(self, form_Database):
        if not form_Database.objectName():
            form_Database.setObjectName(u"form_Database")
        form_Database.resize(1221, 724)
        self.frame_Database = QFrame(form_Database)
        self.frame_Database.setObjectName(u"frame_Database")
        self.frame_Database.setGeometry(QRect(30, 20, 1141, 411))
        self.frame_Database.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Database.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_AUTH = QFrame(self.frame_Database)
        self.frame_AUTH.setObjectName(u"frame_AUTH")
        self.frame_AUTH.setGeometry(QRect(910, 10, 211, 221))
        self.frame_AUTH.setMinimumSize(QSize(211, 0))
        self.frame_AUTH.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_AUTH.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_AUTH)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radio_X509 = QRadioButton(self.frame_AUTH)
        self.radio_X509.setObjectName(u"radio_X509")

        self.gridLayout_3.addWidget(self.radio_X509, 4, 0, 1, 1)

        self.radio_LDAP = QRadioButton(self.frame_AUTH)
        self.radio_LDAP.setObjectName(u"radio_LDAP")

        self.gridLayout_3.addWidget(self.radio_LDAP, 3, 0, 1, 1)

        self.radio_SHA256 = QRadioButton(self.frame_AUTH)
        self.radio_SHA256.setObjectName(u"radio_SHA256")

        self.gridLayout_3.addWidget(self.radio_SHA256, 2, 0, 1, 1)

        self.radio_KERBEROS = QRadioButton(self.frame_AUTH)
        self.radio_KERBEROS.setObjectName(u"radio_KERBEROS")

        self.gridLayout_3.addWidget(self.radio_KERBEROS, 6, 0, 1, 1)

        self.radio_SHA1 = QRadioButton(self.frame_AUTH)
        self.radio_SHA1.setObjectName(u"radio_SHA1")

        self.gridLayout_3.addWidget(self.radio_SHA1, 1, 0, 1, 1)

        self.radio_AWS = QRadioButton(self.frame_AUTH)
        self.radio_AWS.setObjectName(u"radio_AWS")

        self.gridLayout_3.addWidget(self.radio_AWS, 5, 0, 1, 1)

        self.radio_KERBEROS_2 = QRadioButton(self.frame_AUTH)
        self.radio_KERBEROS_2.setObjectName(u"radio_KERBEROS_2")

        self.gridLayout_3.addWidget(self.radio_KERBEROS_2, 7, 0, 1, 1)

        self.label_authtypes = QLabel(self.frame_AUTH)
        self.label_authtypes.setObjectName(u"label_authtypes")

        self.gridLayout_3.addWidget(self.label_authtypes, 0, 0, 1, 1)

        self.frame_MONGODB = QFrame(self.frame_Database)
        self.frame_MONGODB.setObjectName(u"frame_MONGODB")
        self.frame_MONGODB.setGeometry(QRect(20, 10, 431, 251))
        self.frame_MONGODB.setMinimumSize(QSize(431, 0))
        self.frame_MONGODB.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_MONGODB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_MONGODB)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.text_DbName = QTextEdit(self.frame_MONGODB)
        self.text_DbName.setObjectName(u"text_DbName")

        self.gridLayout_2.addWidget(self.text_DbName, 6, 1, 1, 1)

        self.text_AuthSource = QTextEdit(self.frame_MONGODB)
        self.text_AuthSource.setObjectName(u"text_AuthSource")

        self.gridLayout_2.addWidget(self.text_AuthSource, 5, 1, 1, 1)

        self.label_port = QLabel(self.frame_MONGODB)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout_2.addWidget(self.label_port, 2, 0, 1, 1)

        self.text_Host = QTextEdit(self.frame_MONGODB)
        self.text_Host.setObjectName(u"text_Host")

        self.gridLayout_2.addWidget(self.text_Host, 1, 1, 1, 1)

        self.label_password = QLabel(self.frame_MONGODB)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout_2.addWidget(self.label_password, 4, 0, 1, 1)

        self.text_Password = QTextEdit(self.frame_MONGODB)
        self.text_Password.setObjectName(u"text_Password")

        self.gridLayout_2.addWidget(self.text_Password, 4, 1, 1, 1)

        self.label_authsource = QLabel(self.frame_MONGODB)
        self.label_authsource.setObjectName(u"label_authsource")

        self.gridLayout_2.addWidget(self.label_authsource, 5, 0, 1, 1)

        self.text_Username = QTextEdit(self.frame_MONGODB)
        self.text_Username.setObjectName(u"text_Username")

        self.gridLayout_2.addWidget(self.text_Username, 3, 1, 1, 1)

        self.label_host = QLabel(self.frame_MONGODB)
        self.label_host.setObjectName(u"label_host")

        self.gridLayout_2.addWidget(self.label_host, 1, 0, 1, 1)

        self.label_dbname = QLabel(self.frame_MONGODB)
        self.label_dbname.setObjectName(u"label_dbname")

        self.gridLayout_2.addWidget(self.label_dbname, 6, 0, 1, 1)

        self.label_username = QLabel(self.frame_MONGODB)
        self.label_username.setObjectName(u"label_username")

        self.gridLayout_2.addWidget(self.label_username, 3, 0, 1, 1)

        self.text_Port = QTextEdit(self.frame_MONGODB)
        self.text_Port.setObjectName(u"text_Port")

        self.gridLayout_2.addWidget(self.text_Port, 2, 1, 1, 1)

        self.label_mongocredentials = QLabel(self.frame_MONGODB)
        self.label_mongocredentials.setObjectName(u"label_mongocredentials")

        self.gridLayout_2.addWidget(self.label_mongocredentials, 0, 1, 1, 1)

        self.frame_SSH = QFrame(self.frame_Database)
        self.frame_SSH.setObjectName(u"frame_SSH")
        self.frame_SSH.setGeometry(QRect(470, 10, 421, 181))
        self.frame_SSH.setMinimumSize(QSize(421, 0))
        self.frame_SSH.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_SSH.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_SSH)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_ssh_password = QLabel(self.frame_SSH)
        self.label_ssh_password.setObjectName(u"label_ssh_password")

        self.gridLayout.addWidget(self.label_ssh_password, 4, 0, 1, 1)

        self.text_SSH_Username = QTextEdit(self.frame_SSH)
        self.text_SSH_Username.setObjectName(u"text_SSH_Username")

        self.gridLayout.addWidget(self.text_SSH_Username, 3, 1, 1, 1)

        self.checkbox_SSH = QCheckBox(self.frame_SSH)
        self.checkbox_SSH.setObjectName(u"checkbox_SSH")

        self.gridLayout.addWidget(self.checkbox_SSH, 0, 0, 1, 1)

        self.label_sshcredentials = QLabel(self.frame_SSH)
        self.label_sshcredentials.setObjectName(u"label_sshcredentials")

        self.gridLayout.addWidget(self.label_sshcredentials, 0, 1, 1, 1)

        self.label_ssh_host = QLabel(self.frame_SSH)
        self.label_ssh_host.setObjectName(u"label_ssh_host")

        self.gridLayout.addWidget(self.label_ssh_host, 1, 0, 1, 1)

        self.label_ssh_port = QLabel(self.frame_SSH)
        self.label_ssh_port.setObjectName(u"label_ssh_port")

        self.gridLayout.addWidget(self.label_ssh_port, 2, 0, 1, 1)

        self.label_ssh_username = QLabel(self.frame_SSH)
        self.label_ssh_username.setObjectName(u"label_ssh_username")

        self.gridLayout.addWidget(self.label_ssh_username, 3, 0, 1, 1)

        self.text_SSH_Host = QTextEdit(self.frame_SSH)
        self.text_SSH_Host.setObjectName(u"text_SSH_Host")

        self.gridLayout.addWidget(self.text_SSH_Host, 1, 1, 1, 1)

        self.text_SSH_Password = QTextEdit(self.frame_SSH)
        self.text_SSH_Password.setObjectName(u"text_SSH_Password")

        self.gridLayout.addWidget(self.text_SSH_Password, 4, 1, 1, 1)

        self.text_SSH_Port = QTextEdit(self.frame_SSH)
        self.text_SSH_Port.setObjectName(u"text_SSH_Port")

        self.gridLayout.addWidget(self.text_SSH_Port, 2, 1, 1, 1)

        self.widget = QWidget(self.frame_Database)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 271, 1101, 121))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.text_MongoUri = QPlainTextEdit(self.widget)
        self.text_MongoUri.setObjectName(u"text_MongoUri")

        self.gridLayout_4.addWidget(self.text_MongoUri, 0, 0, 1, 3)

        self.button_TestConnection = QPushButton(self.widget)
        self.button_TestConnection.setObjectName(u"button_TestConnection")

        self.gridLayout_4.addWidget(self.button_TestConnection, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.button_Connect = QPushButton(self.widget)
        self.button_Connect.setObjectName(u"button_Connect")

        self.gridLayout_4.addWidget(self.button_Connect, 1, 2, 1, 1)


        self.retranslateUi(form_Database)

        QMetaObject.connectSlotsByName(form_Database)
    # setupUi

    def retranslateUi(self, form_Database):
        form_Database.setWindowTitle(QCoreApplication.translate("form_Database", u"Database Configuration Settings", None))
        self.radio_X509.setText(QCoreApplication.translate("form_Database", u"MONGODB-&X509  ", None))
        self.radio_LDAP.setText(QCoreApplication.translate("form_Database", u"L&DAP", None))
        self.radio_SHA256.setText(QCoreApplication.translate("form_Database", u"SCRAM-SHA-&256  ", None))
        self.radio_KERBEROS.setText(QCoreApplication.translate("form_Database", u"&GSSAPI (Kerberos)  ", None))
        self.radio_SHA1.setText(QCoreApplication.translate("form_Database", u"SCRAM-SHA-&1  ", None))
        self.radio_AWS.setText(QCoreApplication.translate("form_Database", u"M&ONGODB-AWS  ", None))
        self.radio_KERBEROS_2.setText(QCoreApplication.translate("form_Database", u"P&LAIN  ", None))
        self.label_authtypes.setText(QCoreApplication.translate("form_Database", u"Authentication Types:", None))
        self.label_port.setText(QCoreApplication.translate("form_Database", u"PORT:", None))
        self.label_password.setText(QCoreApplication.translate("form_Database", u"PASSWORD:", None))
        self.label_authsource.setText(QCoreApplication.translate("form_Database", u"AUTH SOURCE:", None))
        self.label_host.setText(QCoreApplication.translate("form_Database", u"HOST:", None))
        self.label_dbname.setText(QCoreApplication.translate("form_Database", u"DB NAME:", None))
        self.label_username.setText(QCoreApplication.translate("form_Database", u"USERNAME:", None))
        self.label_mongocredentials.setText(QCoreApplication.translate("form_Database", u"MongoDB Credentials:", None))
        self.label_ssh_password.setText(QCoreApplication.translate("form_Database", u"SSH PASSWORD:", None))
        self.checkbox_SSH.setText(QCoreApplication.translate("form_Database", u"SSH", None))
        self.label_sshcredentials.setText(QCoreApplication.translate("form_Database", u"SSH Credentials", None))
        self.label_ssh_host.setText(QCoreApplication.translate("form_Database", u"SSH HOST:", None))
        self.label_ssh_port.setText(QCoreApplication.translate("form_Database", u"SSH PORT:", None))
        self.label_ssh_username.setText(QCoreApplication.translate("form_Database", u"SSH USERNAME:", None))
        self.text_MongoUri.setPlainText(QCoreApplication.translate("form_Database", u"MONGO-URI:\n"
"", None))
        self.button_TestConnection.setText(QCoreApplication.translate("form_Database", u"Test Connection", None))
        self.button_Connect.setText(QCoreApplication.translate("form_Database", u"Connect", None))
    # retranslateUi

