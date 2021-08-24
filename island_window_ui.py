# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'island_window_uilhzlvE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_IslandDataWindow(object):
    def setupUi(self, IslandDataWindow):
        if not IslandDataWindow.objectName():
            IslandDataWindow.setObjectName(u"IslandDataWindow")
        IslandDataWindow.resize(640, 180)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(67)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IslandDataWindow.sizePolicy().hasHeightForWidth())
        IslandDataWindow.setSizePolicy(sizePolicy)
        IslandDataWindow.setMinimumSize(QSize(640, 180))
        IslandDataWindow.setMaximumSize(QSize(640, 180))
        self.gridLayoutWidget_10 = QWidget(IslandDataWindow)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 10, 271, 101))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.IslandMembersCount = QLineEdit(self.gridLayoutWidget_10)
        self.IslandMembersCount.setObjectName(u"IslandMembersCount")
        self.IslandMembersCount.setEnabled(True)
        self.IslandMembersCount.setMouseTracking(True)
        self.IslandMembersCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_9.addWidget(self.IslandMembersCount, 2, 1, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_10)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_9.addWidget(self.label_41, 1, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_10)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_9.addWidget(self.label_40, 2, 2, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_10)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_9.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_10)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_9.addWidget(self.label_39, 2, 0, 1, 1)

        self.IslandCategory = QLineEdit(self.gridLayoutWidget_10)
        self.IslandCategory.setObjectName(u"IslandCategory")
        self.IslandCategory.setEnabled(True)
        self.IslandCategory.setMouseTracking(True)
        self.IslandCategory.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_9.addWidget(self.IslandCategory, 1, 1, 1, 3)

        self.PostsCount = QLineEdit(self.gridLayoutWidget_10)
        self.PostsCount.setObjectName(u"PostsCount")
        self.PostsCount.setEnabled(True)
        self.PostsCount.setMouseTracking(True)
        self.PostsCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_9.addWidget(self.PostsCount, 2, 3, 1, 1)

        self.IslandName = QLineEdit(self.gridLayoutWidget_10)
        self.IslandName.setObjectName(u"IslandName")
        self.IslandName.setEnabled(True)
        self.IslandName.setMouseTracking(True)
        self.IslandName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_9.addWidget(self.IslandName, 0, 1, 1, 3)

        self.label_42 = QLabel(self.gridLayoutWidget_10)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_9.addWidget(self.label_42, 3, 0, 1, 1)

        self.IslandMasterName = QLineEdit(self.gridLayoutWidget_10)
        self.IslandMasterName.setObjectName(u"IslandMasterName")
        self.IslandMasterName.setEnabled(True)
        self.IslandMasterName.setMouseTracking(True)
        self.IslandMasterName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_9.addWidget(self.IslandMasterName, 3, 1, 1, 3)

        self.gridLayoutWidget_11 = QWidget(IslandDataWindow)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(290, 10, 331, 101))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_11)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)

        self.IslandIntroduction = QTextEdit(self.gridLayoutWidget_11)
        self.IslandIntroduction.setObjectName(u"IslandIntroduction")
        self.IslandIntroduction.setFocusPolicy(Qt.NoFocus)
        self.IslandIntroduction.setOverwriteMode(False)

        self.gridLayout_10.addWidget(self.IslandIntroduction, 0, 1, 2, 1)

        self.CopyButton = QPushButton(IslandDataWindow)
        self.CopyButton.setObjectName(u"CopyButton")
        self.CopyButton.setGeometry(QRect(520, 130, 101, 31))
        font = QFont()
        font.setPointSize(13)
        self.CopyButton.setFont(font)
        self.gridLayoutWidget_3 = QWidget(IslandDataWindow)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 130, 211, 36))
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


        self.retranslateUi(IslandDataWindow)

        QMetaObject.connectSlotsByName(IslandDataWindow)
    # setupUi

    def retranslateUi(self, IslandDataWindow):
        IslandDataWindow.setWindowTitle(QCoreApplication.translate("IslandDataWindow", u"\u5c0f\u5c9b\u4fe1\u606f - ", None))
        self.IslandMembersCount.setText("")
        self.label_41.setText(QCoreApplication.translate("IslandDataWindow", u"\u5206\u7c7b", None))
        self.label_40.setText(QCoreApplication.translate("IslandDataWindow", u"\u5e16\u5b50\u6570", None))
        self.label_38.setText(QCoreApplication.translate("IslandDataWindow", u"\u5c0f\u5c9b\u540d\u79f0", None))
        self.label_39.setText(QCoreApplication.translate("IslandDataWindow", u"\u5c9b\u6c11\u6570", None))
        self.IslandCategory.setText("")
        self.PostsCount.setText("")
        self.IslandName.setText("")
        self.label_42.setText(QCoreApplication.translate("IslandDataWindow", u"\u5c9b\u4e3b", None))
        self.IslandMasterName.setText("")
        self.label_4.setText(QCoreApplication.translate("IslandDataWindow", u"\u5c0f\u5c9b\u7b80\u4ecb", None))
        self.CopyButton.setText(QCoreApplication.translate("IslandDataWindow", u"\u590d\u5236\u4fe1\u606f", None))
        self.Version_2.setText("")
        self.label_20.setText(QCoreApplication.translate("IslandDataWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("IslandDataWindow", u"\u6570\u636e\u83b7\u53d6\u65f6\u95f4\uff1a", None))
        self.DataTime_2.setText("")
    # retranslateUi

