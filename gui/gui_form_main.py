# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindowTzjdMP.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_form_MainWindow(object):
    def setupUi(self, form_MainWindow):
        if not form_MainWindow.objectName():
            form_MainWindow.setObjectName(u"form_MainWindow")
        form_MainWindow.resize(652, 399)
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
        self.layoutWidget.setGeometry(QRect(50, 70, 161, 81))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_DATABASE = QPushButton(self.layoutWidget)
        self.button_DATABASE.setObjectName(u"button_DATABASE")

        self.verticalLayout.addWidget(self.button_DATABASE)

        self.button_EBAY = QPushButton(self.layoutWidget)
        self.button_EBAY.setObjectName(u"button_EBAY")

        self.verticalLayout.addWidget(self.button_EBAY)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(270, 80, 256, 192))
        form_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(form_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 652, 31))
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
        self.button_DATABASE.setText(QCoreApplication.translate("form_MainWindow", u"Database", None))
        self.button_EBAY.setText(QCoreApplication.translate("form_MainWindow", u"Ebay API", None))
        self.menuFIle.setTitle(QCoreApplication.translate("form_MainWindow", u"Fi&le", None))
    # retranslateUi

