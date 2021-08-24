# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_window_uiKQXNWX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_UserDataWindow(object):
    def setupUi(self, UserDataWindow):
        if not UserDataWindow.objectName():
            UserDataWindow.setObjectName(u"UserDataWindow")
        UserDataWindow.resize(640, 340)
        UserDataWindow.setMinimumSize(QSize(640, 340))
        UserDataWindow.setMaximumSize(QSize(640, 340))
        self.gridLayoutWidget = QWidget(UserDataWindow)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 271, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)

        self.FPCount = QLineEdit(self.gridLayoutWidget)
        self.FPCount.setObjectName(u"FPCount")
        self.FPCount.setEnabled(True)
        self.FPCount.setMouseTracking(True)
        self.FPCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.FPCount, 5, 1, 1, 1)

        self.FansCount = QLineEdit(self.gridLayoutWidget)
        self.FansCount.setObjectName(u"FansCount")
        self.FansCount.setEnabled(True)
        self.FansCount.setMouseTracking(True)
        self.FansCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.FansCount, 2, 3, 1, 1)

        self.ArticlesCount = QLineEdit(self.gridLayoutWidget)
        self.ArticlesCount.setObjectName(u"ArticlesCount")
        self.ArticlesCount.setEnabled(True)
        self.ArticlesCount.setMouseTracking(True)
        self.ArticlesCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.ArticlesCount, 3, 1, 1, 1)

        self.TotalAssetsCount = QLineEdit(self.gridLayoutWidget)
        self.TotalAssetsCount.setObjectName(u"TotalAssetsCount")
        self.TotalAssetsCount.setEnabled(True)
        self.TotalAssetsCount.setMouseTracking(True)
        self.TotalAssetsCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.TotalAssetsCount, 4, 3, 1, 1)

        self.LikesCount = QLineEdit(self.gridLayoutWidget)
        self.LikesCount.setObjectName(u"LikesCount")
        self.LikesCount.setEnabled(True)
        self.LikesCount.setMouseTracking(True)
        self.LikesCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.LikesCount, 4, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SexUnknown = QRadioButton(self.gridLayoutWidget)
        self.SexUnknown.setObjectName(u"SexUnknown")
        self.SexUnknown.setEnabled(False)
        self.SexUnknown.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.SexUnknown)

        self.SexMale = QRadioButton(self.gridLayoutWidget)
        self.SexMale.setObjectName(u"SexMale")
        self.SexMale.setEnabled(False)
        self.SexMale.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.SexMale)

        self.SexFemale = QRadioButton(self.gridLayoutWidget)
        self.SexFemale.setObjectName(u"SexFemale")
        self.SexFemale.setEnabled(False)
        self.SexFemale.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.SexFemale)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 3)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Wordage = QLineEdit(self.gridLayoutWidget)
        self.Wordage.setObjectName(u"Wordage")
        self.Wordage.setEnabled(True)
        self.Wordage.setMouseTracking(True)
        self.Wordage.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.Wordage, 3, 3, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)

        self.BadgesList = QListWidget(self.gridLayoutWidget)
        self.BadgesList.setObjectName(u"BadgesList")
        self.BadgesList.setFocusPolicy(Qt.NoFocus)
        self.BadgesList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.BadgesList.setFlow(QListView.TopToBottom)
        self.BadgesList.setProperty("isWrapping", False)
        self.BadgesList.setResizeMode(QListView.Fixed)
        self.BadgesList.setViewMode(QListView.ListMode)
        self.BadgesList.setModelColumn(0)

        self.gridLayout.addWidget(self.BadgesList, 6, 1, 1, 3)

        self.FTNCount = QLineEdit(self.gridLayoutWidget)
        self.FTNCount.setObjectName(u"FTNCount")
        self.FTNCount.setEnabled(True)
        self.FTNCount.setMouseTracking(True)
        self.FTNCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.FTNCount, 5, 3, 1, 1)

        self.FollowersCount = QLineEdit(self.gridLayoutWidget)
        self.FollowersCount.setObjectName(u"FollowersCount")
        self.FollowersCount.setEnabled(True)
        self.FollowersCount.setMouseTracking(True)
        self.FollowersCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.FollowersCount, 2, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)

        self.UserName = QLineEdit(self.gridLayoutWidget)
        self.UserName.setObjectName(u"UserName")
        self.UserName.setEnabled(True)
        self.UserName.setMouseTracking(True)
        self.UserName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.UserName, 0, 1, 1, 3)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(UserDataWindow)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(300, 10, 321, 281))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)

        self.VIPLevel = QLineEdit(self.gridLayoutWidget_2)
        self.VIPLevel.setObjectName(u"VIPLevel")
        self.VIPLevel.setEnabled(True)
        self.VIPLevel.setMouseTracking(True)
        self.VIPLevel.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.VIPLevel, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)

        self.VIPExpireDate = QLineEdit(self.gridLayoutWidget_2)
        self.VIPExpireDate.setObjectName(u"VIPExpireDate")
        self.VIPExpireDate.setEnabled(True)
        self.VIPExpireDate.setMouseTracking(True)
        self.VIPExpireDate.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.VIPExpireDate, 2, 1, 1, 1)

        self.NextAnniversaryDay = QLineEdit(self.gridLayoutWidget_2)
        self.NextAnniversaryDay.setObjectName(u"NextAnniversaryDay")
        self.NextAnniversaryDay.setEnabled(True)
        self.NextAnniversaryDay.setMouseTracking(True)
        self.NextAnniversaryDay.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.NextAnniversaryDay, 3, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)

        self.LastUpdateTime = QLineEdit(self.gridLayoutWidget_2)
        self.LastUpdateTime.setObjectName(u"LastUpdateTime")
        self.LastUpdateTime.setEnabled(True)
        self.LastUpdateTime.setMouseTracking(True)
        self.LastUpdateTime.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.LastUpdateTime, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 157, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.IntroductionText = QTextEdit(self.gridLayoutWidget_2)
        self.IntroductionText.setObjectName(u"IntroductionText")
        self.IntroductionText.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.IntroductionText, 4, 1, 2, 1)

        self.label_15 = QLabel(UserDataWindow)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(959, 279, 72, 20))
        self.CopyButton = QPushButton(UserDataWindow)
        self.CopyButton.setObjectName(u"CopyButton")
        self.CopyButton.setGeometry(QRect(520, 300, 101, 31))
        font = QFont()
        font.setPointSize(13)
        self.CopyButton.setFont(font)
        self.gridLayoutWidget_3 = QWidget(UserDataWindow)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 300, 211, 36))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Version = QLabel(self.gridLayoutWidget_3)
        self.Version.setObjectName(u"Version")

        self.gridLayout_3.addWidget(self.Version, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)

        self.DataTime = QLabel(self.gridLayoutWidget_3)
        self.DataTime.setObjectName(u"DataTime")

        self.gridLayout_3.addWidget(self.DataTime, 1, 1, 1, 1)

        QWidget.setTabOrder(self.SexUnknown, self.SexMale)
        QWidget.setTabOrder(self.SexMale, self.SexFemale)
        QWidget.setTabOrder(self.SexFemale, self.BadgesList)
        QWidget.setTabOrder(self.BadgesList, self.CopyButton)

        self.retranslateUi(UserDataWindow)

        self.BadgesList.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(UserDataWindow)
    # setupUi

    def retranslateUi(self, UserDataWindow):
        UserDataWindow.setWindowTitle(QCoreApplication.translate("UserDataWindow", u"\u7528\u6237\u4fe1\u606f - ", None))
        self.label_11.setText(QCoreApplication.translate("UserDataWindow", u"\u5fbd\u7ae0\u5217\u8868", None))
        self.FPCount.setText("")
        self.FansCount.setText("")
        self.ArticlesCount.setText("")
        self.TotalAssetsCount.setText("")
        self.LikesCount.setText("")
        self.label_4.setText(QCoreApplication.translate("UserDataWindow", u"\u7c89\u4e1d\u6570", None))
        self.label_10.setText(QCoreApplication.translate("UserDataWindow", u"\u7b80\u4e66\u8d1d", None))
        self.SexUnknown.setText(QCoreApplication.translate("UserDataWindow", u"\u672a\u77e5", None))
        self.SexMale.setText(QCoreApplication.translate("UserDataWindow", u"\u7537", None))
        self.SexFemale.setText(QCoreApplication.translate("UserDataWindow", u"\u5973", None))
        self.label.setText(QCoreApplication.translate("UserDataWindow", u"\u7528\u6237\u6635\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("UserDataWindow", u"\u5173\u6ce8\u6570", None))
        self.Wordage.setText("")
        self.label_6.setText(QCoreApplication.translate("UserDataWindow", u"\u603b\u5b57\u6570", None))
        self.FTNCount.setText("")
        self.FollowersCount.setText("")
        self.label_8.setText(QCoreApplication.translate("UserDataWindow", u"\u603b\u8d44\u4ea7", None))
        self.UserName.setText("")
        self.label_2.setText(QCoreApplication.translate("UserDataWindow", u"\u6027\u522b", None))
        self.label_5.setText(QCoreApplication.translate("UserDataWindow", u"\u6587\u7ae0\u6570", None))
        self.label_7.setText(QCoreApplication.translate("UserDataWindow", u"\u83b7\u8d5e\u6570", None))
        self.label_9.setText(QCoreApplication.translate("UserDataWindow", u"\u7b80\u4e66\u94bb", None))
        self.label_16.setText(QCoreApplication.translate("UserDataWindow", u"\u4f1a\u5458\u8fc7\u671f\u65f6\u95f4", None))
        self.VIPLevel.setText("")
        self.label_12.setText(QCoreApplication.translate("UserDataWindow", u"\u4e2a\u4eba\u7b80\u4ecb", None))
        self.label_14.setText(QCoreApplication.translate("UserDataWindow", u"\u4f1a\u5458\u7b49\u7ea7", None))
        self.VIPExpireDate.setText("")
        self.NextAnniversaryDay.setText("")
        self.label_13.setText(QCoreApplication.translate("UserDataWindow", u"\u6700\u540e\u66f4\u65b0\u65f6\u95f4", None))
        self.label_17.setText(QCoreApplication.translate("UserDataWindow", u"\u4e0b\u6b21\u5468\u5e74\u5e86\u65f6\u95f4", None))
        self.LastUpdateTime.setText("")
        self.label_15.setText(QCoreApplication.translate("UserDataWindow", u"\u6700\u540e\u66f4\u65b0\u65f6\u95f4", None))
        self.CopyButton.setText(QCoreApplication.translate("UserDataWindow", u"\u590d\u5236\u4fe1\u606f", None))
        self.Version.setText("")
        self.label_20.setText(QCoreApplication.translate("UserDataWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("UserDataWindow", u"\u6570\u636e\u83b7\u53d6\u65f6\u95f4\uff1a", None))
        self.DataTime.setText("")
    # retranslateUi

