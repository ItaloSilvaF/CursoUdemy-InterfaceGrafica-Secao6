# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 197)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnGeraCPF = QtWidgets.QPushButton(self.centralwidget)
        self.btnGeraCPF.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnGeraCPF.setFont(font)
        self.btnGeraCPF.setObjectName("btnGeraCPF")
        self.gridLayout.addWidget(self.btnGeraCPF, 1, 2, 1, 1)
        self.inputValidaCPF = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValidaCPF.setMinimumSize(QtCore.QSize(50, 30))
        self.inputValidaCPF.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputValidaCPF.setFont(font)
        self.inputValidaCPF.setObjectName("inputValidaCPF")
        self.gridLayout.addWidget(self.inputValidaCPF, 0, 1, 1, 1)
        self.btnValidaCPF = QtWidgets.QPushButton(self.centralwidget)
        self.btnValidaCPF.setMinimumSize(QtCore.QSize(200, 30))
        self.btnValidaCPF.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnValidaCPF.setFont(font)
        self.btnValidaCPF.setObjectName("btnValidaCPF")
        self.gridLayout.addWidget(self.btnValidaCPF, 0, 2, 1, 1)
        self.lineEditRetorno = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRetorno.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lineEditRetorno.setFont(font)
        self.lineEditRetorno.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRetorno.setReadOnly(False)
        self.lineEditRetorno.setObjectName("lineEditRetorno")
        self.gridLayout.addWidget(self.lineEditRetorno, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Gerar CPF:"))
        self.label.setText(_translate("MainWindow", "Validar CPF:"))
        self.btnGeraCPF.setText(_translate("MainWindow", "GERAR"))
        self.btnValidaCPF.setText(_translate("MainWindow", "VALIDAR"))
