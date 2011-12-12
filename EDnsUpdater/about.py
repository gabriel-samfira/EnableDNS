# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Fri Dec  9 18:39:51 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.setWindowModality(QtCore.Qt.WindowModal)
        About.resize(423, 297)
        About.setWindowTitle(QtGui.QApplication.translate("About", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        About.setStyleSheet(_fromUtf8("#label {\n"
"font-weight: bold;\n"
"font-size:22px;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(About)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(About)
        self.label.setText(QtGui.QApplication.translate("About", "EnableDNS Updater", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtGui.QLabel(About)
        self.label_3.setText(QtGui.QApplication.translate("About", "Vesion: 0.01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(About)
        self.label_4.setText(QtGui.QApplication.translate("About", "This is the EnableDNS dynamic update client\n"
"This program is Open Source Software\n"
"and can be downloaded from:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_2 = QtGui.QLabel(About)
        self.label_2.setText(QtGui.QApplication.translate("About", "https://github.com/gabriel-samfira/EnableDNS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.buttonBox = QtGui.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(About)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), About.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        pass

