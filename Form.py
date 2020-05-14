# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(298, 193)
        MainWindow.setMinimumSize(QtCore.QSize(298, 193))
        MainWindow.setMaximumSize(QtCore.QSize(298, 193))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 0, 151, 16))
        self.label.setObjectName("label")
        self.number_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.number_LineEdit.setGeometry(QtCore.QRect(60, 20, 181, 20))
        self.number_LineEdit.setObjectName("number_LineEdit")
        self.checkButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkButton.setGeometry(QtCore.QRect(110, 50, 75, 23))
        self.checkButton.setObjectName("checkButton")
        self.validation_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.validation_LineEdit.setEnabled(False)
        self.validation_LineEdit.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.validation_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.validation_LineEdit.setObjectName("validation_LineEdit")
        self.help_TextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.help_TextEdit.setGeometry(QtCore.QRect(10, 110, 281, 51))
        self.help_TextEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.help_TextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.help_TextEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.help_TextEdit.setReadOnly(True)
        self.help_TextEdit.setObjectName("help_TextEdit")
        self.help_TextEdit.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 298, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CreditCard Validator"))
        self.label.setText(_translate("MainWindow", "Credit card validation"))
        self.number_LineEdit.setInputMask(_translate("MainWindow", "9999 9999 9999 999900"))
        self.checkButton.setText(_translate("MainWindow", "Check"))
