# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ebaypYjjNV.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_form_EbayAPI(object):
    def setupUi(self, form_EbayAPI):
        if not form_EbayAPI.objectName():
            form_EbayAPI.setObjectName(u"form_EbayAPI")
        form_EbayAPI.resize(683, 353)
        self.frame = QFrame(form_EbayAPI)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 50, 451, 221))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_SITE_ID = QComboBox(self.frame)
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.addItem("")
        self.comboBox_SITE_ID.setObjectName(u"comboBox_SITE_ID")

        self.gridLayout.addWidget(self.comboBox_SITE_ID, 0, 2, 1, 1)

        self.button_IMPORT_CONFIG = QPushButton(self.frame)
        self.button_IMPORT_CONFIG.setObjectName(u"button_IMPORT_CONFIG")

        self.gridLayout.addWidget(self.button_IMPORT_CONFIG, 3, 2, 1, 1)

        self.label_domain = QLabel(self.frame)
        self.label_domain.setObjectName(u"label_domain")

        self.gridLayout.addWidget(self.label_domain, 2, 0, 1, 1)

        self.label_site_id = QLabel(self.frame)
        self.label_site_id.setObjectName(u"label_site_id")

        self.gridLayout.addWidget(self.label_site_id, 0, 0, 1, 2)

        self.text_Domain = QTextEdit(self.frame)
        self.text_Domain.setObjectName(u"text_Domain")

        self.gridLayout.addWidget(self.text_Domain, 2, 1, 1, 2)

        self.label_app_id = QLabel(self.frame)
        self.label_app_id.setObjectName(u"label_app_id")

        self.gridLayout.addWidget(self.label_app_id, 1, 0, 1, 1)

        self.button_CONNECT = QPushButton(self.frame)
        self.button_CONNECT.setObjectName(u"button_CONNECT")

        self.gridLayout.addWidget(self.button_CONNECT, 4, 2, 1, 1)

        self.label_config_file = QLabel(self.frame)
        self.label_config_file.setObjectName(u"label_config_file")

        self.gridLayout.addWidget(self.label_config_file, 3, 0, 1, 2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)

        self.text_AppID = QTextEdit(self.frame)
        self.text_AppID.setObjectName(u"text_AppID")

        self.gridLayout.addWidget(self.text_AppID, 1, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(form_EbayAPI)

        QMetaObject.connectSlotsByName(form_EbayAPI)
    # setupUi

    def retranslateUi(self, form_EbayAPI):
        form_EbayAPI.setWindowTitle(QCoreApplication.translate("form_EbayAPI", u"Ebay API Settings", None))
        self.comboBox_SITE_ID.setItemText(0, QCoreApplication.translate("form_EbayAPI", u"EBAY-US", None))
        self.comboBox_SITE_ID.setItemText(1, QCoreApplication.translate("form_EbayAPI", u"EBAY-ENCA", None))
        self.comboBox_SITE_ID.setItemText(2, QCoreApplication.translate("form_EbayAPI", u"EBAY-GB", None))
        self.comboBox_SITE_ID.setItemText(3, QCoreApplication.translate("form_EbayAPI", u"EBAY-AU", None))
        self.comboBox_SITE_ID.setItemText(4, QCoreApplication.translate("form_EbayAPI", u"EBAY-AT", None))
        self.comboBox_SITE_ID.setItemText(5, QCoreApplication.translate("form_EbayAPI", u"EBAY-FRBE", None))
        self.comboBox_SITE_ID.setItemText(6, QCoreApplication.translate("form_EbayAPI", u"EBAY-FR", None))
        self.comboBox_SITE_ID.setItemText(7, QCoreApplication.translate("form_EbayAPI", u"EBAY-DE", None))
        self.comboBox_SITE_ID.setItemText(8, QCoreApplication.translate("form_EbayAPI", u"EBAY-MOTOR", None))
        self.comboBox_SITE_ID.setItemText(9, QCoreApplication.translate("form_EbayAPI", u"EBAY-IT", None))
        self.comboBox_SITE_ID.setItemText(10, QCoreApplication.translate("form_EbayAPI", u"EBAY-NLBE", None))
        self.comboBox_SITE_ID.setItemText(11, QCoreApplication.translate("form_EbayAPI", u"EBAY-NL", None))
        self.comboBox_SITE_ID.setItemText(12, QCoreApplication.translate("form_EbayAPI", u"EBAY-ES", None))
        self.comboBox_SITE_ID.setItemText(13, QCoreApplication.translate("form_EbayAPI", u"EBAY-CH", None))
        self.comboBox_SITE_ID.setItemText(14, QCoreApplication.translate("form_EbayAPI", u"EBAY-HK", None))
        self.comboBox_SITE_ID.setItemText(15, QCoreApplication.translate("form_EbayAPI", u"EBAY-IE", None))
        self.comboBox_SITE_ID.setItemText(16, QCoreApplication.translate("form_EbayAPI", u"EBAY-MY", None))
        self.comboBox_SITE_ID.setItemText(17, QCoreApplication.translate("form_EbayAPI", u"EBAY-FRCA", None))
        self.comboBox_SITE_ID.setItemText(18, QCoreApplication.translate("form_EbayAPI", u"EBAY-PH", None))
        self.comboBox_SITE_ID.setItemText(19, QCoreApplication.translate("form_EbayAPI", u"EBAY-PL", None))
        self.comboBox_SITE_ID.setItemText(20, QCoreApplication.translate("form_EbayAPI", u"EBAY-SG", None))

        self.button_IMPORT_CONFIG.setText(QCoreApplication.translate("form_EbayAPI", u"Import Config", None))
        self.label_domain.setText(QCoreApplication.translate("form_EbayAPI", u"DOMAIN:", None))
        self.label_site_id.setText(QCoreApplication.translate("form_EbayAPI", u"SITE ID:", None))
        self.label_app_id.setText(QCoreApplication.translate("form_EbayAPI", u"APP ID:", None))
        self.button_CONNECT.setText(QCoreApplication.translate("form_EbayAPI", u"Connect", None))
        self.label_config_file.setText(QCoreApplication.translate("form_EbayAPI", u"CONFIG FILE:", None))
        self.pushButton.setText(QCoreApplication.translate("form_EbayAPI", u"Test API", None))
    # retranslateUi

