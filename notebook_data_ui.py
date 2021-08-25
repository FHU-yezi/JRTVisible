# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notebook_data_uiZsepxB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_NotebookDataWindow(object):
    def setupUi(self, NotebookDataWindow):
        if not NotebookDataWindow.objectName():
            NotebookDataWindow.setObjectName(u"NotebookDataWindow")
        NotebookDataWindow.resize(640, 200)
        NotebookDataWindow.setMinimumSize(QSize(640, 200))
        NotebookDataWindow.setMaximumSize(QSize(640, 200))
        self.gridLayoutWidget_13 = QWidget(NotebookDataWindow)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(10, 10, 271, 126))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.TotalWordage = QLineEdit(self.gridLayoutWidget_13)
        self.TotalWordage.setObjectName(u"TotalWordage")
        self.TotalWordage.setEnabled(True)
        self.TotalWordage.setMouseTracking(True)
        self.TotalWordage.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.TotalWordage, 2, 3, 1, 1)

        self.SubscribersCount = QLineEdit(self.gridLayoutWidget_13)
        self.SubscribersCount.setObjectName(u"SubscribersCount")
        self.SubscribersCount.setEnabled(True)
        self.SubscribersCount.setMouseTracking(True)
        self.SubscribersCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.SubscribersCount, 3, 1, 1, 3)

        self.Author = QLineEdit(self.gridLayoutWidget_13)
        self.Author.setObjectName(u"Author")
        self.Author.setEnabled(True)
        self.Author.setMouseTracking(True)
        self.Author.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.Author, 1, 1, 1, 3)

        self.label_48 = QLabel(self.gridLayoutWidget_13)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_13.addWidget(self.label_48, 3, 0, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_13)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_13.addWidget(self.label_47, 2, 0, 1, 1)

        self.label_45 = QLabel(self.gridLayoutWidget_13)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_13.addWidget(self.label_45, 2, 2, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget_13)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_13.addWidget(self.label_46, 0, 0, 1, 1)

        self.ArticlesCount = QLineEdit(self.gridLayoutWidget_13)
        self.ArticlesCount.setObjectName(u"ArticlesCount")
        self.ArticlesCount.setEnabled(True)
        self.ArticlesCount.setMouseTracking(True)
        self.ArticlesCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.ArticlesCount, 2, 1, 1, 1)

        self.NotebookName = QLineEdit(self.gridLayoutWidget_13)
        self.NotebookName.setObjectName(u"NotebookName")
        self.NotebookName.setEnabled(True)
        self.NotebookName.setMouseTracking(True)
        self.NotebookName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.NotebookName, 0, 1, 1, 3)

        self.label_44 = QLabel(self.gridLayoutWidget_13)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_13.addWidget(self.label_44, 1, 0, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget_13)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_13.addWidget(self.label_49, 4, 0, 1, 1)

        self.UpdateTime = QLineEdit(self.gridLayoutWidget_13)
        self.UpdateTime.setObjectName(u"UpdateTime")
        self.UpdateTime.setEnabled(True)
        self.UpdateTime.setMouseTracking(True)
        self.UpdateTime.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.UpdateTime, 4, 1, 1, 3)

        self.gridLayoutWidget_14 = QWidget(NotebookDataWindow)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(290, 10, 331, 121))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_14)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_14.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.RecentlyArticles = QListWidget(self.gridLayoutWidget_14)
        self.RecentlyArticles.setObjectName(u"RecentlyArticles")
        self.RecentlyArticles.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_14.addWidget(self.RecentlyArticles, 0, 1, 2, 1)

        self.CopyButton = QPushButton(NotebookDataWindow)
        self.CopyButton.setObjectName(u"CopyButton")
        self.CopyButton.setGeometry(QRect(520, 150, 101, 31))
        font = QFont()
        font.setPointSize(13)
        self.CopyButton.setFont(font)
        self.gridLayoutWidget_4 = QWidget(NotebookDataWindow)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 150, 211, 36))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Version = QLabel(self.gridLayoutWidget_4)
        self.Version.setObjectName(u"Version")

        self.gridLayout_4.addWidget(self.Version, 0, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)

        self.DataTime = QLabel(self.gridLayoutWidget_4)
        self.DataTime.setObjectName(u"DataTime")

        self.gridLayout_4.addWidget(self.DataTime, 1, 1, 1, 1)

        QWidget.setTabOrder(self.RecentlyArticles, self.CopyButton)

        self.retranslateUi(NotebookDataWindow)

        QMetaObject.connectSlotsByName(NotebookDataWindow)
    # setupUi

    def retranslateUi(self, NotebookDataWindow):
        NotebookDataWindow.setWindowTitle(QCoreApplication.translate("NotebookDataWindow", u"\u6587\u96c6\u4fe1\u606f - ", None))
        self.TotalWordage.setText("")
        self.SubscribersCount.setText("")
        self.Author.setText("")
        self.label_48.setText(QCoreApplication.translate("NotebookDataWindow", u"\u5173\u6ce8\u8005\u6570", None))
        self.label_47.setText(QCoreApplication.translate("NotebookDataWindow", u"\u6587\u7ae0\u6570", None))
        self.label_45.setText(QCoreApplication.translate("NotebookDataWindow", u"\u603b\u5b57\u6570", None))
        self.label_46.setText(QCoreApplication.translate("NotebookDataWindow", u"\u6587\u96c6\u540d\u79f0", None))
        self.ArticlesCount.setText("")
        self.NotebookName.setText("")
        self.label_44.setText(QCoreApplication.translate("NotebookDataWindow", u"\u4f5c\u8005", None))
        self.label_49.setText(QCoreApplication.translate("NotebookDataWindow", u"\u66f4\u65b0\u65f6\u95f4", None))
        self.UpdateTime.setText("")
        self.label_6.setText(QCoreApplication.translate("NotebookDataWindow", u"\u6700\u65b0\u6587\u7ae0", None))
        self.CopyButton.setText(QCoreApplication.translate("NotebookDataWindow", u"\u590d\u5236\u4fe1\u606f", None))
        self.Version.setText("")
        self.label_21.setText(QCoreApplication.translate("NotebookDataWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("NotebookDataWindow", u"\u6570\u636e\u83b7\u53d6\u65f6\u95f4\uff1a", None))
        self.DataTime.setText("")
    # retranslateUi

