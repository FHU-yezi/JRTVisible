# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'article_window_uiVpJkab.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ArticleDataWindow(object):
    def setupUi(self, ArticleDataWindow):
        if not ArticleDataWindow.objectName():
            ArticleDataWindow.setObjectName(u"ArticleDataWindow")
        ArticleDataWindow.resize(640, 280)
        ArticleDataWindow.setMinimumSize(QSize(640, 280))
        ArticleDataWindow.setMaximumSize(QSize(640, 280))
        self.CopyButton = QPushButton(ArticleDataWindow)
        self.CopyButton.setObjectName(u"CopyButton")
        self.CopyButton.setGeometry(QRect(520, 230, 101, 31))
        font = QFont()
        font.setPointSize(13)
        self.CopyButton.setFont(font)
        self.gridLayoutWidget_5 = QWidget(ArticleDataWindow)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 271, 204))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PublishTime = QLineEdit(self.gridLayoutWidget_5)
        self.PublishTime.setObjectName(u"PublishTime")
        self.PublishTime.setEnabled(True)
        self.PublishTime.setMouseTracking(True)
        self.PublishTime.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.PublishTime, 2, 1, 1, 3)

        self.label_38 = QLabel(self.gridLayoutWidget_5)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_5.addWidget(self.label_38, 6, 2, 1, 1)

        self.AuthorName = QLineEdit(self.gridLayoutWidget_5)
        self.AuthorName.setObjectName(u"AuthorName")
        self.AuthorName.setEnabled(True)
        self.AuthorName.setMouseTracking(True)
        self.AuthorName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.AuthorName, 1, 1, 1, 3)

        self.CommentsCount = QLineEdit(self.gridLayoutWidget_5)
        self.CommentsCount.setObjectName(u"CommentsCount")
        self.CommentsCount.setEnabled(True)
        self.CommentsCount.setMouseTracking(True)
        self.CommentsCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.CommentsCount, 5, 3, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_5)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 2, 0, 1, 1)

        self.ArticleName = QLineEdit(self.gridLayoutWidget_5)
        self.ArticleName.setObjectName(u"ArticleName")
        self.ArticleName.setEnabled(True)
        self.ArticleName.setMouseTracking(True)
        self.ArticleName.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.ArticleName, 0, 1, 1, 3)

        self.LikesCount = QLineEdit(self.gridLayoutWidget_5)
        self.LikesCount.setObjectName(u"LikesCount")
        self.LikesCount.setEnabled(True)
        self.LikesCount.setMouseTracking(True)
        self.LikesCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.LikesCount, 5, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_5)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 1, 0, 1, 1)

        self.Wordage = QLineEdit(self.gridLayoutWidget_5)
        self.Wordage.setObjectName(u"Wordage")
        self.Wordage.setEnabled(True)
        self.Wordage.setMouseTracking(True)
        self.Wordage.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.Wordage, 4, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 4, 2, 1, 1)

        self.UpdateTime = QLineEdit(self.gridLayoutWidget_5)
        self.UpdateTime.setObjectName(u"UpdateTime")
        self.UpdateTime.setEnabled(True)
        self.UpdateTime.setMouseTracking(True)
        self.UpdateTime.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.UpdateTime, 3, 1, 1, 3)

        self.MostValuableCommentsCount = QLineEdit(self.gridLayoutWidget_5)
        self.MostValuableCommentsCount.setObjectName(u"MostValuableCommentsCount")
        self.MostValuableCommentsCount.setEnabled(True)
        self.MostValuableCommentsCount.setMouseTracking(True)
        self.MostValuableCommentsCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.MostValuableCommentsCount, 6, 1, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 5, 2, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_5)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_5.addWidget(self.label_37, 3, 0, 1, 1)

        self.PaidType = QLineEdit(self.gridLayoutWidget_5)
        self.PaidType.setObjectName(u"PaidType")
        self.PaidType.setEnabled(True)
        self.PaidType.setMouseTracking(True)
        self.PaidType.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.PaidType, 6, 3, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_5)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_5.addWidget(self.label_36, 6, 0, 1, 1)

        self.FPCount = QLineEdit(self.gridLayoutWidget_5)
        self.FPCount.setObjectName(u"FPCount")
        self.FPCount.setEnabled(True)
        self.FPCount.setMouseTracking(True)
        self.FPCount.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.FPCount, 4, 3, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_5)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_5.addWidget(self.label_39, 7, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 4, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_5)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_5.addWidget(self.label_40, 7, 2, 1, 1)

        self.CommentStatus = QLineEdit(self.gridLayoutWidget_5)
        self.CommentStatus.setObjectName(u"CommentStatus")
        self.CommentStatus.setEnabled(True)
        self.CommentStatus.setMouseTracking(True)
        self.CommentStatus.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.CommentStatus, 7, 1, 1, 1)

        self.ReprintStatus = QLineEdit(self.gridLayoutWidget_5)
        self.ReprintStatus.setObjectName(u"ReprintStatus")
        self.ReprintStatus.setEnabled(True)
        self.ReprintStatus.setMouseTracking(True)
        self.ReprintStatus.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.ReprintStatus, 7, 3, 1, 1)

        self.gridLayoutWidget_6 = QWidget(ArticleDataWindow)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(300, 10, 321, 204))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_6)
        self.label.setObjectName(u"label")

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.ArticleContent = QTextEdit(self.gridLayoutWidget_6)
        self.ArticleContent.setObjectName(u"ArticleContent")
        self.ArticleContent.setFocusPolicy(Qt.NoFocus)
        self.ArticleContent.setOverwriteMode(False)

        self.gridLayout_7.addWidget(self.ArticleContent, 0, 1, 2, 1)

        self.gridLayoutWidget_7 = QWidget(ArticleDataWindow)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 230, 211, 36))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Version = QLabel(self.gridLayoutWidget_7)
        self.Version.setObjectName(u"Version")

        self.gridLayout_6.addWidget(self.Version, 0, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_7)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)

        self.DataTime = QLabel(self.gridLayoutWidget_7)
        self.DataTime.setObjectName(u"DataTime")

        self.gridLayout_6.addWidget(self.DataTime, 1, 1, 1, 1)


        self.retranslateUi(ArticleDataWindow)

        QMetaObject.connectSlotsByName(ArticleDataWindow)
    # setupUi

    def retranslateUi(self, ArticleDataWindow):
        ArticleDataWindow.setWindowTitle(QCoreApplication.translate("ArticleDataWindow", u"\u6587\u7ae0\u4fe1\u606f - ", None))
        self.CopyButton.setText(QCoreApplication.translate("ArticleDataWindow", u"\u590d\u5236\u4fe1\u606f", None))
        self.PublishTime.setText("")
        self.label_38.setText(QCoreApplication.translate("ArticleDataWindow", u"\u4ed8\u8d39\u7c7b\u578b", None))
        self.AuthorName.setText("")
        self.CommentsCount.setText("")
        self.label_28.setText(QCoreApplication.translate("ArticleDataWindow", u"\u53d1\u5e03\u65f6\u95f4", None))
        self.ArticleName.setText("")
        self.LikesCount.setText("")
        self.label_26.setText(QCoreApplication.translate("ArticleDataWindow", u"\u6587\u7ae0\u540d", None))
        self.label_27.setText(QCoreApplication.translate("ArticleDataWindow", u"\u4f5c\u8005\u540d", None))
        self.Wordage.setText("")
        self.label_9.setText(QCoreApplication.translate("ArticleDataWindow", u"\u83b7\u94bb\u91cf", None))
        self.UpdateTime.setText("")
        self.MostValuableCommentsCount.setText("")
        self.label_30.setText(QCoreApplication.translate("ArticleDataWindow", u"\u8bc4\u8bba\u6570", None))
        self.label_37.setText(QCoreApplication.translate("ArticleDataWindow", u"\u66f4\u65b0\u65f6\u95f4", None))
        self.PaidType.setText("")
        self.label_36.setText(QCoreApplication.translate("ArticleDataWindow", u"\u7cbe\u9009\u8bc4\u8bba\u6570", None))
        self.FPCount.setText("")
        self.label_39.setText(QCoreApplication.translate("ArticleDataWindow", u"\u8bc4\u8bba\u72b6\u6001", None))
        self.label_29.setText(QCoreApplication.translate("ArticleDataWindow", u"\u5b57\u6570", None))
        self.label_10.setText(QCoreApplication.translate("ArticleDataWindow", u"\u83b7\u8d5e\u6570", None))
        self.label_40.setText(QCoreApplication.translate("ArticleDataWindow", u"\u8f6c\u8f7d\u72b6\u6001", None))
        self.CommentStatus.setText("")
        self.ReprintStatus.setText("")
        self.label.setText(QCoreApplication.translate("ArticleDataWindow", u"\u6587\u7ae0\u5185\u5bb9", None))
        self.Version.setText("")
        self.label_21.setText(QCoreApplication.translate("ArticleDataWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("ArticleDataWindow", u"\u6570\u636e\u83b7\u53d6\u65f6\u95f4\uff1a", None))
        self.DataTime.setText("")
    # retranslateUi

