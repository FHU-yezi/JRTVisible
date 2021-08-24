# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_uiFYIeeP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 120)
        MainWindow.setMinimumSize(QSize(640, 120))
        MainWindow.setMaximumSize(QSize(640, 120))
        self.horizontalLayoutWidget = QWidget(MainWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 20, 581, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.UrlType = QComboBox(self.horizontalLayoutWidget)
        self.UrlType.addItem("")
        self.UrlType.addItem("")
        self.UrlType.addItem("")
        self.UrlType.addItem("")
        self.UrlType.addItem("")
        self.UrlType.addItem("")
        self.UrlType.setObjectName(u"UrlType")
        font = QFont()
        font.setPointSize(13)
        self.UrlType.setFont(font)

        self.horizontalLayout.addWidget(self.UrlType)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.UrlInput = QLineEdit(self.horizontalLayoutWidget)
        self.UrlInput.setObjectName(u"UrlInput")
        self.UrlInput.setFont(font)

        self.horizontalLayout.addWidget(self.UrlInput)

        self.GetDataButton = QPushButton(self.horizontalLayoutWidget)
        self.GetDataButton.setObjectName(u"GetDataButton")
        self.GetDataButton.setFont(font)

        self.horizontalLayout.addWidget(self.GetDataButton)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JRT \u53ef\u89c6\u5316\u67e5\u8be2\u5de5\u5177", None))
        self.UrlType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u68c0\u6d4b", None))
        self.UrlType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
        self.UrlType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u6587\u7ae0", None))
        self.UrlType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e13\u9898", None))
        self.UrlType.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5c0f\u5c9b", None))
        self.UrlType.setItemText(5, QCoreApplication.translate("MainWindow", u"\u6587\u96c6", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u94fe\u63a5\uff1a", None))
        self.GetDataButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
    # retranslateUi

