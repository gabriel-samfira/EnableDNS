# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Dec 11 03:03:02 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 250)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 250))
        MainWindow.setMaximumSize(QtCore.QSize(600, 250))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "EnableDNS updater", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/updater/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("#centralwidget {\n"
"background: url(\":/updater/background-small.png\");\n"
"}\n"
"\n"
"#SideWidget {\n"
"background: url(\":/updater/eDNS-logo200.png\");\n"
"}\n"
"\n"
"#groupBox {\n"
"color: white;\n"
"border: 1px solid #555;\n"
"border-radius: 3px;\n"
"padding: 4px;\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.SideWidget = QtGui.QWidget(self.centralwidget)
        self.SideWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SideWidget.setObjectName(_fromUtf8("SideWidget"))
        self.horizontalLayout.addWidget(self.SideWidget)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet(_fromUtf8(".QLabel {\n"
"color: white;\n"
"}"))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 351, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.AcctInfo = QtGui.QLabel(self.layoutWidget)
        self.AcctInfo.setText(QtGui.QApplication.translate("MainWindow", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.AcctInfo.setObjectName(_fromUtf8("AcctInfo"))
        self.gridLayout.addWidget(self.AcctInfo, 0, 0, 1, 1)
        self.ch_acct = QtGui.QPushButton(self.layoutWidget)
        self.ch_acct.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ch_acct.setText(QtGui.QApplication.translate("MainWindow", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_acct.setObjectName(_fromUtf8("ch_acct"))
        self.gridLayout.addWidget(self.ch_acct, 0, 1, 1, 1)
        self.DomInfo = QtGui.QLabel(self.layoutWidget)
        self.DomInfo.setText(QtGui.QApplication.translate("MainWindow", "Domain", None, QtGui.QApplication.UnicodeUTF8))
        self.DomInfo.setObjectName(_fromUtf8("DomInfo"))
        self.gridLayout.addWidget(self.DomInfo, 1, 0, 1, 1)
        self.ch_dom = QtGui.QPushButton(self.layoutWidget)
        self.ch_dom.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ch_dom.setText(QtGui.QApplication.translate("MainWindow", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_dom.setObjectName(_fromUtf8("ch_dom"))
        self.gridLayout.addWidget(self.ch_dom, 1, 1, 1, 1)
        self.UpStat = QtGui.QLabel(self.layoutWidget)
        self.UpStat.setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.UpStat.setObjectName(_fromUtf8("UpStat"))
        self.gridLayout.addWidget(self.UpStat, 2, 0, 1, 1)
        self.refresh = QtGui.QPushButton(self.layoutWidget)
        self.refresh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.refresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.gridLayout.addWidget(self.refresh, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHide = QtGui.QAction(MainWindow)
        self.actionHide.setText(QtGui.QApplication.translate("MainWindow", "Hide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHide.setObjectName(_fromUtf8("actionHide"))
        self.actionQuit_2 = QtGui.QAction(MainWindow)
        self.actionQuit_2.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_2.setObjectName(_fromUtf8("actionQuit_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionHide)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_2)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

import resources_rc
