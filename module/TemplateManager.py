# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python32\template.ui'
#
# Created: Thu Oct 18 14:45:47 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import *
from PyQt4.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class TemplateManager(QDialog):
    def __init__( self, parent = None ):
        super( TemplateManager, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(425, 487)
        self.setWindowTitle(QtGui.QApplication.translate("self", "模板管理", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 461))
        self.groupBox.setTitle(QtGui.QApplication.translate("self", "模板列表", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 251, 431))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 10, 115, 83))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("self", "设置模板", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.templateButton = QtGui.QPushButton(self.groupBox_2)
        self.templateButton.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.templateButton.setText(QtGui.QApplication.translate("self", "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.templateButton.setObjectName(_fromUtf8("templateButton"))
        self.groupBox_3 = QtGui.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 100, 115, 83))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("self", "入库", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.templateupdateButton = QtGui.QPushButton(self.groupBox_3)
        self.templateupdateButton.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.templateupdateButton.setText(QtGui.QApplication.translate("self", "模板入库", None, QtGui.QApplication.UnicodeUTF8))
        self.templateupdateButton.setObjectName(_fromUtf8("templateupdateButton"))
        self.groupBox_4 = QtGui.QGroupBox(self)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 210, 120, 251))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("self", "下载", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 81, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.updateButton = QtGui.QPushButton(self.layoutWidget)
        self.updateButton.setText(QtGui.QApplication.translate("self", "更新", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.verticalLayout.addWidget(self.updateButton)
        self.openButton = QtGui.QPushButton(self.layoutWidget)
        self.openButton.setText(QtGui.QApplication.translate("self", "打开", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.verticalLayout.addWidget(self.openButton)
        self.downloadButton = QtGui.QPushButton(self.layoutWidget)
        self.downloadButton.setText(QtGui.QApplication.translate("self", "下载", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.verticalLayout.addWidget(self.downloadButton)
        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setText(QtGui.QApplication.translate("self", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.verticalLayout.addWidget(self.cancelButton)
        self.layoutWidget1 = QtGui.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        #self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        pass


