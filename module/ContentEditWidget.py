#!/usr/bin/python
#coding=utf-8
# 内容编辑窗口类
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ContentEditWidget( QWidget):
    def __init__( self, parent=None):
        super( ContentEditWidget, self).__init__( parent)

        self.setupUI()
        print "ContentEditWidget init.."
        
    def setupUI(self):
        print "ContentEditWidget setupUI.."
        self.setWindowTitle( self.tr("内容编辑窗口"))

        self.m_treeLeft = QTreeView( self)
        self.m_treeRight = QTreeView( self)

        self.m_btToRight = QPushButton()
        self.m_btToLeft = QPushButton()
        self.m_btToRightAll = QPushButton()
        self.m_btToLeftAll = QPushButton()

        miniWid = 70
        miniHei = 30
        self.m_btToRight.setText( self.tr("右移"))
        self.m_btToLeft.setText( self.tr("左移"))
        self.m_btToRightAll.setText( self.tr("全右移"))
        self.m_btToLeftAll.setText( self.tr("全左移"))
        self.m_btToRight.setMinimumHeight( miniHei)
        self.m_btToLeft.setMinimumHeight( miniHei)
        self.m_btToRightAll.setMinimumHeight( miniHei)
        self.m_btToLeftAll.setMinimumWidth( miniWid)
        self.m_btToLeftAll.setMinimumHeight( miniHei)
        
        self.m_vCenterLayout = QVBoxLayout()
        self.m_vCenterLayout.addWidget( self.m_btToRight)
        self.m_vCenterLayout.addWidget( self.m_btToLeft)
        self.m_vCenterLayout.addWidget( self.m_btToRightAll)
        self.m_vCenterLayout.addWidget( self.m_btToLeftAll)

        self.m_hMainLayout = QHBoxLayout()
        self.m_hMainLayout.addWidget( self.m_treeLeft)
        self.m_hMainLayout.addLayout( self.m_vCenterLayout)
        self.m_hMainLayout.addWidget( self.m_treeRight)

        self.setLayout( self.m_hMainLayout)
        """菜单-文件
        """
        
        





