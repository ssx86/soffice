# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python32\report.ui'
#
# Created: Thu Oct 18 14:48:05 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ReportManager(object):
    def __init__( self, parent = None ):
	print "report Manager"
        super( ReportManage, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(425, 487)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "报告管理", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 461))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "报告列表", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 251, 431))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 10, 115, 83))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "设置报告", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.reportButton = QtGui.QPushButton(self.groupBox_2)
        self.reportButton.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.reportButton.setText(QtGui.QApplication.translate("Dialog", "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.reportButton.setObjectName(_fromUtf8("reportButton"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 100, 115, 83))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "入库", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.reportupdateButton = QtGui.QPushButton(self.groupBox_3)
        self.reportupdateButton.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.reportupdateButton.setText(QtGui.QApplication.translate("Dialog", "报告入库", None, QtGui.QApplication.UnicodeUTF8))
        self.reportupdateButton.setObjectName(_fromUtf8("reportupdateButton"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 210, 120, 251))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "下载", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 81, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.updateButton = QtGui.QPushButton(self.layoutWidget)
        self.updateButton.setText(QtGui.QApplication.translate("Dialog", "更新", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.verticalLayout.addWidget(self.updateButton)
        self.openButton = QtGui.QPushButton(self.layoutWidget)
        self.openButton.setText(QtGui.QApplication.translate("Dialog", "打开", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.verticalLayout.addWidget(self.openButton)
        self.downloadButton = QtGui.QPushButton(self.layoutWidget)
        self.downloadButton.setText(QtGui.QApplication.translate("Dialog", "下载", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.verticalLayout.addWidget(self.downloadButton)
        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setText(QtGui.QApplication.translate("Dialog", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.verticalLayout.addWidget(self.cancelButton)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        #self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        pass

