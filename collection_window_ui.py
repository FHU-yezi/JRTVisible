# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collection_window_uiPsmFgn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_CollectionDataWindow(object):
    def setupUi(self, CollectionDataWindow):
        if not CollectionDataWindow.objectName():
            CollectionDataWindow.setObjectName(u"CollectionDataWindow")
        CollectionDataWindow.resize(640, 200)
        CollectionDataWindow.setMinimumSize(QSize(640, 200))
        CollectionDataWindow.setMaximumSize(QSize(640, 200))
        self.gridLayoutWidget_7 = QWidget(CollectionDataWindow)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 10, 271, 121))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.gridLayoutWidget_7)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 3, 0, 1, 1)

        self.ArticlesCount = QLineEdit(self.gridLayoutWidget_7)
        self.ArticlesCount.setObjectName(u"ArticlesCount")
        self.ArticlesCount.setEnabled(True)
        self.ArticlesCount.setMouseTracking(True)
        self.ArticlesCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_6.addWidget(self.ArticlesCount, 1, 1, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_7)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 5, 0, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_7)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 4, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_7)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_6.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_7)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 1, 0, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_7)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_6.addWidget(self.label_32, 1, 2, 1, 1)

        self.SubscribersCount = QLineEdit(self.gridLayoutWidget_7)
        self.SubscribersCount.setObjectName(u"SubscribersCount")
        self.SubscribersCount.setEnabled(True)
        self.SubscribersCount.setMouseTracking(True)
        self.SubscribersCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_6.addWidget(self.SubscribersCount, 1, 3, 1, 1)

        self.CollectionName = QLineEdit(self.gridLayoutWidget_7)
        self.CollectionName.setObjectName(u"CollectionName")
        self.CollectionName.setEnabled(True)
        self.CollectionName.setMouseTracking(True)
        self.CollectionName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_6.addWidget(self.CollectionName, 0, 1, 1, 3)

        self.MainEditerName = QLineEdit(self.gridLayoutWidget_7)
        self.MainEditerName.setObjectName(u"MainEditerName")
        self.MainEditerName.setEnabled(True)
        self.MainEditerName.setMouseTracking(True)
        self.MainEditerName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_6.addWidget(self.MainEditerName, 5, 1, 1, 3)

        self.ArticleUpdateTime = QLineEdit(self.gridLayoutWidget_7)
        self.ArticleUpdateTime.setObjectName(u"ArticleUpdateTime")
        self.ArticleUpdateTime.setEnabled(True)
        self.ArticleUpdateTime.setMouseTracking(True)
        self.ArticleUpdateTime.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_6.addWidget(self.ArticleUpdateTime, 4, 1, 1, 3)

        self.ImformationUpdateTime = QLineEdit(self.gridLayoutWidget_7)
        self.ImformationUpdateTime.setObjectName(u"ImformationUpdateTime")
        self.ImformationUpdateTime.setEnabled(True)
        self.ImformationUpdateTime.setMouseTracking(True)
        self.ImformationUpdateTime.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_6.addWidget(self.ImformationUpdateTime, 3, 1, 1, 3)

        self.gridLayoutWidget_8 = QWidget(CollectionDataWindow)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(290, 10, 331, 121))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.CollectionIntroduction = QTextEdit(self.gridLayoutWidget_8)
        self.CollectionIntroduction.setObjectName(u"CollectionIntroduction")
        self.CollectionIntroduction.setFocusPolicy(Qt.NoFocus)
        self.CollectionIntroduction.setOverwriteMode(False)

        self.gridLayout_8.addWidget(self.CollectionIntroduction, 0, 1, 2, 1)

        self.CopyButton_ = QPushButton(CollectionDataWindow)
        self.CopyButton_.setObjectName(u"CopyButton_")
        self.CopyButton_.setGeometry(QRect(520, 150, 101, 31))
        font = QFont()
        font.setPointSize(13)
        self.CopyButton_.setFont(font)
        self.gridLayoutWidget_3 = QWidget(CollectionDataWindow)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 150, 211, 36))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Version_2 = QLabel(self.gridLayoutWidget_3)
        self.Version_2.setObjectName(u"Version_2")

        self.gridLayout_3.addWidget(self.Version_2, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)

        self.DataTime_2 = QLabel(self.gridLayoutWidget_3)
        self.DataTime_2.setObjectName(u"DataTime_2")

        self.gridLayout_3.addWidget(self.DataTime_2, 1, 1, 1, 1)


        self.retranslateUi(CollectionDataWindow)

        QMetaObject.connectSlotsByName(CollectionDataWindow)
    # setupUi

    def retranslateUi(self, CollectionDataWindow):
        CollectionDataWindow.setWindowTitle(QCoreApplication.translate("CollectionDataWindow", u"\u4e13\u9898\u4fe1\u606f - ", None))
        self.label_34.setText(QCoreApplication.translate("CollectionDataWindow", u"\u4fe1\u606f\u66f4\u65b0\u65f6\u95f4", None))
        self.ArticlesCount.setText("")
        self.label_36.setText(QCoreApplication.translate("CollectionDataWindow", u"\u4e3b\u7f16\u540d", None))
        self.label_35.setText(QCoreApplication.translate("CollectionDataWindow", u"\u6587\u7ae0\u66f4\u65b0\u65f6\u95f4", None))
        self.label_31.setText(QCoreApplication.translate("CollectionDataWindow", u"\u4e13\u9898\u540d\u79f0", None))
        self.label_33.setText(QCoreApplication.translate("CollectionDataWindow", u"\u6536\u5f55\u6587\u7ae0\u6570", None))
        self.label_32.setText(QCoreApplication.translate("CollectionDataWindow", u"\u5173\u6ce8\u8005\u6570", None))
        self.SubscribersCount.setText("")
        self.CollectionName.setText("")
        self.MainEditerName.setText("")
        self.ArticleUpdateTime.setText("")
        self.ImformationUpdateTime.setText("")
        self.label_2.setText(QCoreApplication.translate("CollectionDataWindow", u"\u4e13\u9898\u7b80\u4ecb", None))
        self.CopyButton_.setText(QCoreApplication.translate("CollectionDataWindow", u"\u590d\u5236\u4fe1\u606f", None))
        self.Version_2.setText("")
        self.label_20.setText(QCoreApplication.translate("CollectionDataWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("CollectionDataWindow", u"\u6570\u636e\u83b7\u53d6\u65f6\u95f4\uff1a", None))
        self.DataTime_2.setText("")
    # retranslateUi

