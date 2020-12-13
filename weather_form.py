# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 366)
        Dialog.setStyleSheet(u"background-color: rgb(75, 75, 75);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(26, 122, 361, 231))
        self.label.setStyleSheet(u"color: rgb(220, 220, 220);\n"
                                 "font: 14pt \"Arial\";")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 381, 41))
        self.lineEdit.setStyleSheet(u"color: rgb(238, 203, 7);\n"
                                    "font: 75 18pt \"Arial\";\n"
                                    "background-color: #1d1c21;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 70, 361, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                      "	font: 18pt \"Century Gothic\";\n"
                                      "	color: #f2b824;\n"
                                      "	background-color: #1d1c21;\n"
                                      "	border: none;\n"
                                      "}\n"
                                      "\n"
                                      "QPushBotton:hover {\n"
                                      "	color: #f2c44e;\n"
                                      "	background-color: #3a3c42;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "	color: #eb7b13;\n"
                                      "}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("Dialog", u"\u041f\u041e\u041b\u0423\u0427\u0418\u0422\u042c", None))
    # retranslateUi
