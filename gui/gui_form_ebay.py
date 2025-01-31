# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ebayzQJvGb.ui'
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
        form_EbayAPI.resize(531, 286)
        self.frame = QFrame(form_EbayAPI)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 20, 411, 201))
        self.frame.setMinimumSize(QSize(411, 201))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_site_id = QLabel(self.frame)
        self.label_site_id.setObjectName(u"label_site_id")
        self.label_site_id.setMinimumSize(QSize(249, 33))

        self.gridLayout.addWidget(self.label_site_id, 0, 0, 1, 2)

        self.comboBox_SITE_ID = QComboBox(self.frame)
        self.comboBox_SITE_ID.setObjectName(u"comboBox_SITE_ID")
        self.comboBox_SITE_ID.setMinimumSize(QSize(142, 33))

        self.gridLayout.addWidget(self.comboBox_SITE_ID, 0, 2, 1, 1)

        self.label_app_id = QLabel(self.frame)
        self.label_app_id.setObjectName(u"label_app_id")
        self.label_app_id.setMinimumSize(QSize(122, 33))

        self.gridLayout.addWidget(self.label_app_id, 1, 0, 1, 1)

        self.text_AppID = QTextEdit(self.frame)
        self.text_AppID.setObjectName(u"text_AppID")
        self.text_AppID.setMinimumSize(QSize(269, 33))

        self.gridLayout.addWidget(self.text_AppID, 1, 1, 1, 2)

        self.label_domain = QLabel(self.frame)
        self.label_domain.setObjectName(u"label_domain")
        self.label_domain.setMinimumSize(QSize(122, 32))

        self.gridLayout.addWidget(self.label_domain, 2, 0, 1, 1)

        self.text_Domain = QTextEdit(self.frame)
        self.text_Domain.setObjectName(u"text_Domain")
        self.text_Domain.setMinimumSize(QSize(269, 32))

        self.gridLayout.addWidget(self.text_Domain, 2, 1, 1, 2)

        self.label_config_file = QLabel(self.frame)
        self.label_config_file.setObjectName(u"label_config_file")
        self.label_config_file.setMinimumSize(QSize(122, 33))

        self.gridLayout.addWidget(self.label_config_file, 3, 0, 1, 1)

        self.button_IMPORT_CONFIG = QPushButton(self.frame)
        self.button_IMPORT_CONFIG.setObjectName(u"button_IMPORT_CONFIG")
        self.button_IMPORT_CONFIG.setMinimumSize(QSize(142, 33))

        self.gridLayout.addWidget(self.button_IMPORT_CONFIG, 3, 2, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(122, 32))

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.button_CONNECT = QPushButton(self.frame)
        self.button_CONNECT.setObjectName(u"button_CONNECT")
        self.button_CONNECT.setMinimumSize(QSize(142, 32))

        self.gridLayout.addWidget(self.button_CONNECT, 4, 2, 1, 1)


        self.retranslateUi(form_EbayAPI)

        QMetaObject.connectSlotsByName(form_EbayAPI)
    # setupUi

    def retranslateUi(self, form_EbayAPI):
        form_EbayAPI.setWindowTitle(QCoreApplication.translate("form_EbayAPI", u"Ebay API Settings", None))
        self.label_site_id.setText(QCoreApplication.translate("form_EbayAPI", u"SITE ID:", None))
        self.label_app_id.setText(QCoreApplication.translate("form_EbayAPI", u"APP ID:", None))
        self.label_domain.setText(QCoreApplication.translate("form_EbayAPI", u"DOMAIN:", None))
        self.label_config_file.setText(QCoreApplication.translate("form_EbayAPI", u"CONFIG FILE:", None))
        self.button_IMPORT_CONFIG.setText(QCoreApplication.translate("form_EbayAPI", u"Import Config", None))
        self.pushButton.setText(QCoreApplication.translate("form_EbayAPI", u"Test API", None))
        self.button_CONNECT.setText(QCoreApplication.translate("form_EbayAPI", u"Connect", None))
    # retranslateUi

