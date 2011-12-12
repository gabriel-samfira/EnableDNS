# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Fri Dec  9 15:37:05 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.setWindowModality(QtCore.Qt.WindowModal)
        Login.resize(452, 240)
        Login.setMinimumSize(QtCore.QSize(452, 240))
        Login.setMaximumSize(QtCore.QSize(452, 240))
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "EnableDNS Login", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout = QtGui.QHBoxLayout(Login)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.password = QtGui.QLineEdit(Login)
        self.password.setText(_fromUtf8(""))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Login)
        self.label_3.setText(QtGui.QApplication.translate("Login", "EnableDNS login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.username = QtGui.QLineEdit(Login)
        self.username.setText(_fromUtf8(""))
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Login)
        self.label.setText(QtGui.QApplication.translate("Login", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setText(QtGui.QApplication.translate("Login", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 2)
        self.status = QtGui.QLabel(Login)
        self.status.setText(_fromUtf8(""))
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName(_fromUtf8("status"))
        self.gridLayout.addWidget(self.status, 1, 0, 1, 2)
        self.Buttons = QtGui.QDialogButtonBox(Login)
        self.Buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.Buttons.setObjectName(_fromUtf8("Buttons"))
        self.gridLayout.addWidget(self.Buttons, 7, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.username, self.password)

    def retranslateUi(self, Login):
        pass

