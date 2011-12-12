# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'domains.ui'
#
# Created: Thu Dec  8 13:14:16 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DomainList(object):
    def setupUi(self, DomainList):
        DomainList.setObjectName(_fromUtf8("DomainList"))
        DomainList.setWindowModality(QtCore.Qt.WindowModal)
        DomainList.resize(388, 389)
        DomainList.setWindowTitle(QtGui.QApplication.translate("DomainList", "Domain List", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_2 = QtGui.QVBoxLayout(DomainList)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ok = QtGui.QPushButton(DomainList)
        self.ok.setText(QtGui.QApplication.translate("DomainList", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.gridLayout.addWidget(self.ok, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.Domains = QtGui.QTreeWidget(DomainList)
        self.Domains.setObjectName(_fromUtf8("Domains"))
        self.Domains.headerItem().setText(0, QtGui.QApplication.translate("DomainList", "Domain", None, QtGui.QApplication.UnicodeUTF8))
        self.Domains.headerItem().setText(1, QtGui.QApplication.translate("DomainList", "Record", None, QtGui.QApplication.UnicodeUTF8))
        self.Domains.headerItem().setText(2, QtGui.QApplication.translate("DomainList", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.Domains, 0, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(DomainList)
        QtCore.QMetaObject.connectSlotsByName(DomainList)

    def retranslateUi(self, DomainList):
        pass

