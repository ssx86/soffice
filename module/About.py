# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python32\about.ui'
#
# Created: Thu Oct 18 14:27:38 2012
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

class About(QDialog):
    def __init__( self, parent = None ):
        super( About, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(400, 300)
        self.setWindowTitle(QtGui.QApplication.translate("self", "关于", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 75, 23))
        self.pushButton.setText(QtGui.QApplication.translate("self", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 40, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("self", "辅助报告生成工具", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 321, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("self", "警告：本计算机程序受版权法和国际条件保护，\n"
"如未经授权擅自复制或传播本程序或其中任何部\n"
"分，将受到严厉的民事和刑事制裁，并将在法律\n"
"许可的最大限度内受到起诉", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 341, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("self", "Copyright@北京神州普惠有限公司保留所有权利", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        #self.retranslateUi(self)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        pass



