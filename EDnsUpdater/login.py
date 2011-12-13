# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/login.ui'
#
# Created: Mon Dec 12 12:45:01 2011
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
        Login.resize(452, 300)
        Login.setMinimumSize(QtCore.QSize(452, 300))
        Login.setMaximumSize(QtCore.QSize(452, 300))
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "EnableDNS Login", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/updater/icon128px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(_fromUtf8("#Login {\n"
"background: url(\":/updater/background-small.png\");\n"
"}\n"
"\n"
".QLabel {\n"
"color: white;\n"
"padding: 4px;\n"
"}\n"
""))
        self.horizontalLayout = QtGui.QHBoxLayout(Login)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.password = QtGui.QLineEdit(Login)
        self.password.setText(_fromUtf8(""))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Login)
        self.label_3.setText(QtGui.QApplication.translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">EnableDNS login</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you do not have an account, please click on the link bellow to create one. If you have created an account using one of you social accounts, you must first set a password by accessing <a href=\"https://enabledns.com/profiles/edit\"><span style=\" text-decoration: underline; color:#8ab201;\">your profile page</span></a>.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.username = QtGui.QLineEdit(Login)
        self.username.setText(_fromUtf8(""))
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 3, 1, 1, 1)
        self.label = QtGui.QLabel(Login)
        self.label.setText(QtGui.QApplication.translate("Login", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setText(QtGui.QApplication.translate("Login", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.Buttons = QtGui.QDialogButtonBox(Login)
        self.Buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.Buttons.setObjectName(_fromUtf8("Buttons"))
        self.gridLayout.addWidget(self.Buttons, 7, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Login)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_4.setText(QtGui.QApplication.translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Don\'t have an account? <a href=\"https://enabledns.com/accounts/register/\"><span style=\" text-decoration: underline; color:#8ab20a;\">Create a free account in less then a minute</span></a>. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Forgot your password? <a href=\"https://enabledns.com/accounts/password/reset/\"><span style=\" text-decoration: underline; color:#8ab20a;\">Click here!</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.status = QtGui.QLabel(Login)
        self.status.setText(_fromUtf8(""))
        self.status.setObjectName(_fromUtf8("status"))
        self.gridLayout.addWidget(self.status, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.username, self.password)

    def retranslateUi(self, Login):
        pass

import resource_rc
