# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Ecrin/Desktop/Yeni klasör/oturum.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(188, 260)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 231, 271))
        self.groupBox.setObjectName("groupBox")
        self.btn_oturum = QtWidgets.QPushButton(self.groupBox)
        self.btn_oturum.setGeometry(QtCore.QRect(40, 150, 101, 31))
        self.btn_oturum.setObjectName("btn_oturum")
        self.lbl_sifre = QtWidgets.QLabel(self.groupBox)
        self.lbl_sifre.setGeometry(QtCore.QRect(10, 50, 151, 21))
        self.lbl_sifre.setObjectName("lbl_sifre")
        self.txt_sifre = QtWidgets.QLineEdit(self.groupBox)
        self.txt_sifre.setGeometry(QtCore.QRect(30, 100, 131, 31))
        self.txt_sifre.setObjectName("txt_sifre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 188, 27))
        self.menubar.setObjectName("menubar")
        self.menuGiri = QtWidgets.QMenu(self.menubar)
        self.menuGiri.setObjectName("menuGiri")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGiri.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Giriş"))
        self.btn_oturum.setText(_translate("MainWindow", "Oturum Aç"))
        self.lbl_sifre.setText(_translate("MainWindow", "Şifrenizi Giriniz"))
        self.menuGiri.setTitle(_translate("MainWindow", "Hastane"))

    def __init__ (self):
        self.conn = sqlite3.connect('hastane.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.passwords = ["12345678"]
        
    def entrance(self):
        if self.lbl_sifre == self.passwords[0]:
            pass
        elif self.lbl_sifre == self.passwords[1]:
            pass
        elif self.lbl_sifre == self.passwords[2]:
            pass
        
    def rtn_pass(self):
        # Return the password list
        return self.passwords
