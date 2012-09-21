#!/usr/bin/python
#coding=utf-8
# 工具条管理类
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

        """任务工具
        """
        taskTool = self.m_mainWindow.addToolBar( self.tr("任务工具"))
        
        selectTaskAct = taskTool.addAction( QIcon( self.tr("./img/toolBar/selectTask.png")), self.tr("任务选择"))
        selectTaskAct.triggered.connect( self.m_mainWindow.selectTask)

        updateTaskAct = taskTool.addAction( QIcon( self.tr("./img/toolBar/selectTask.png")), self.tr("更新任务数据"))
        self.connect( updateTaskAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('updateTask()'))

        """文件工具
        """
        fileTool = self.m_mainWindow.addToolBar( self.tr("文件工具"))
        
        fileEditAct = fileTool.addAction( QIcon( self.tr("./img/toolBar/selectTask.png")), self.tr("文件编辑"))
        """self.connect( fileEditAct, SIGNAL('triggered()'), self.m_mainWindow, SLOT('fileEdit()'))"""
        """fileEditAct.triggered.connect( self.m_mainWindow.fileEdit( 0))"""
        """self.connect( fileEditAct, SIGNAL('triggered(bool)'), self.m_mainWindow.fileEdit(bool))"""
        fileEditAct.triggered.connect( self.m_mainWindow.fileEdit)

        previewFileAct = fileTool.addAction( QIcon( self.tr("./img/toolBar/previewReport.png")), self.tr("预览"))
        self.connect( previewFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('previewFile()'))
        





