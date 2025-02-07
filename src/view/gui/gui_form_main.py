# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindowOLfLJv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_form_MainWindow(object):
    def setupUi(self, form_MainWindow):
        if not form_MainWindow.objectName():
            form_MainWindow.setObjectName(u"form_MainWindow")
        form_MainWindow.resize(987, 331)
        self.actionImport_CSV = QAction(form_MainWindow)
        self.actionImport_CSV.setObjectName(u"actionImport_CSV")
        self.actionExport_CSV = QAction(form_MainWindow)
        self.actionExport_CSV.setObjectName(u"actionExport_CSV")
        self.actionExit = QAction(form_MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(form_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 138, 161, 105))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_configure = QLabel(self.layoutWidget)
        self.label_configure.setObjectName(u"label_configure")

        self.verticalLayout.addWidget(self.label_configure)

        self.button_DATABASE = QPushButton(self.layoutWidget)
        self.button_DATABASE.setObjectName(u"button_DATABASE")

        self.verticalLayout.addWidget(self.button_DATABASE)

        self.button_EBAY = QPushButton(self.layoutWidget)
        self.button_EBAY.setObjectName(u"button_EBAY")

        self.verticalLayout.addWidget(self.button_EBAY)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(680, 8, 258, 236))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.button_CsvSearch = QPushButton(self.widget)
        self.button_CsvSearch.setObjectName(u"button_CsvSearch")

        self.gridLayout_2.addWidget(self.button_CsvSearch, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 3)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(240, 170, 401, 71))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.button_EbaySearch = QPushButton(self.widget1)
        self.button_EbaySearch.setObjectName(u"button_EbaySearch")

        self.gridLayout.addWidget(self.button_EbaySearch, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.text_EbayQuery = QPlainTextEdit(self.widget1)
        self.text_EbayQuery.setObjectName(u"text_EbayQuery")

        self.gridLayout.addWidget(self.text_EbayQuery, 0, 0, 1, 3)

        form_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(form_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 31))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        form_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(form_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        form_MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menuFIle.addAction(self.actionImport_CSV)
        self.menuFIle.addAction(self.actionExport_CSV)
        self.menuFIle.addAction(self.actionExit)

        self.retranslateUi(form_MainWindow)

        QMetaObject.connectSlotsByName(form_MainWindow)
    # setupUi

    def retranslateUi(self, form_MainWindow):
        form_MainWindow.setWindowTitle(QCoreApplication.translate("form_MainWindow", u"MainWindow", None))
        self.actionImport_CSV.setText(QCoreApplication.translate("form_MainWindow", u"&Import CSV", None))
        self.actionExport_CSV.setText(QCoreApplication.translate("form_MainWindow", u"&Export CSV", None))
        self.actionExit.setText(QCoreApplication.translate("form_MainWindow", u"E&xit", None))
        self.label_configure.setText(QCoreApplication.translate("form_MainWindow", u"Configure:", None))
        self.button_DATABASE.setText(QCoreApplication.translate("form_MainWindow", u"Database", None))
        self.button_EBAY.setText(QCoreApplication.translate("form_MainWindow", u"Ebay API", None))
        self.button_CsvSearch.setText(QCoreApplication.translate("form_MainWindow", u"PushButton", None))
        self.button_EbaySearch.setText(QCoreApplication.translate("form_MainWindow", u"Search", None))
        self.text_EbayQuery.setPlainText("")
        self.menuFIle.setTitle(QCoreApplication.translate("form_MainWindow", u"Fi&le", None))
    # retranslateUi

