#!/usr/bin/python
#coding=utf-8
# ������������
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ToolBarMgr( QObject):
    def __init__( self, mainWindow, parent=None):
        super( ToolBarMgr, self).__init__( parent)
        
        self.m_mainWindow = mainWindow 

        print "ToolBarMgr init.."
    def setupUI(self):
        print "ToolBarMgr setupUI.."

        """���񹤾�
        """
        taskTool = self.m_mainWindow.addToolBar( self.tr("���񹤾�"))
        
        selectTaskAct = taskTool.addAction( QIcon( self.tr("./img/toolBar/selectTask.png")), self.tr("����ѡ��"))
        selectTaskAct.triggered.connect( self.m_mainWindow.selectTask)

        updateTaskAct = taskTool.addAction( QIcon( self.tr("./img/toolBar/selectTask.png")), self.tr("������������"))
        self.connect( updateTaskAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('updateTask()'))

        """�ļ�����
        """
        fileTool = self.m_mainWindow.addToolBar( self.tr("�ļ�����"))
        
        fileEditAct = fileTool.addAction( QIcon( self.tr("./img/toolBar/selectTask.png")), self.tr("�ļ��༭"))
        """self.connect( fileEditAct, SIGNAL('triggered()'), self.m_mainWindow, SLOT('fileEdit()'))"""
        """fileEditAct.triggered.connect( self.m_mainWindow.fileEdit( 0))"""
        """self.connect( fileEditAct, SIGNAL('triggered(bool)'), self.m_mainWindow.fileEdit(bool))"""
        fileEditAct.triggered.connect( self.m_mainWindow.fileEdit)

        previewFileAct = fileTool.addAction( QIcon( self.tr("./img/toolBar/previewReport.png")), self.tr("Ԥ��"))
        self.connect( previewFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('previewFile()'))
        





