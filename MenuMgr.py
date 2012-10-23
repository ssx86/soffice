#!/usr/bin/python
#coding=utf-8
# 菜单管理类
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MenuMgr( QObject):
    def __init__( self, mainWindow, parent=None):
        super( MenuMgr, self).__init__( parent)
        self.m_menuBar = mainWindow.menuBar()
        self.m_mainWindow = mainWindow 

        print "MenuMgr init.."
    def setupUI(self):
        print "MenuMgr setupUI.."

        """菜单-文件
        """
        fileMenu = self.m_menuBar.addMenu( self.tr("文件"))
        openFileAct = QAction( self.tr("打开"), fileMenu)
        fileMenu.addAction( openFileAct)
        self.connect( openFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('openFile()'))

        saveFileAct = QAction( self.tr("保存"), fileMenu)
        fileMenu.addAction( saveFileAct)
        self.connect( saveFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('saveFile()'))

        saveAsFileAct = QAction( self.tr("另存为"), fileMenu)
        fileMenu.addAction( saveAsFileAct)
        self.connect( saveAsFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('saveAsFile()'))


        previewFileAct = QAction( self.tr("预览"), fileMenu)
        fileMenu.addAction( previewFileAct)
        self.connect( previewFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('previewFile()'))

        """菜单-编辑
        """
        editMenu = self.m_menuBar.addMenu( self.tr("编辑"))
        fileEditAct = QAction( self.tr("文件编辑"), editMenu)
        editMenu.addAction( fileEditAct)
        fileEditAct.triggered.connect( self.m_mainWindow.fileEdit)

        setupAct = QAction( self.tr("打开文档"), editMenu)
        editMenu.addAction( setupAct)
        setupAct.triggered.connect( self.m_mainWindow.openDocument)

        contentEditAct = QAction( self.tr("内容编辑"), editMenu)
        editMenu.addAction( contentEditAct)
        contentEditAct.triggered.connect( self.m_mainWindow.contentEdit)

        """菜单-模板
        """
        templateMenu = self.m_menuBar.addMenu( self.tr("模板"))
        templateManagerAct = QAction( self.tr("模板管理"), templateMenu)
        templateMenu.addAction( templateManagerAct)
        templateManagerAct.triggered.connect( self.m_mainWindow.showTemplateManager )
        #self.connect( templateManagerAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('showTempleteManager()'))

        createTempleteAct = QAction( self.tr("新建"), templateMenu)
        templateMenu.addAction( createTempleteAct)
        self.connect( createTempleteAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('createTemplete()'))

        templateEditAct = QAction( self.tr("编辑"), templateMenu)
        templateMenu.addAction( templateEditAct)
        self.connect( templateEditAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('templateEdit()'))

        templateUploadAct = QAction( self.tr("入库"), templateMenu)
        templateMenu.addAction( templateUploadAct)
        templateUploadAct.triggered.connect( self.m_mainWindow.templateUpload)

        templateDownloadAct = QAction( self.tr("下载"), templateMenu)
        templateMenu.addAction( templateDownloadAct)
        templateDownloadAct.triggered.connect( self.m_mainWindow.templateDownload)

        """菜单-报告
        """
        reportMenu = self.m_menuBar.addMenu( self.tr("报告"))

        reportManagerAct = QAction( self.tr("报告管理"), reportMenu)
        reportMenu.addAction( reportManagerAct)
        reportManagerAct.triggered.connect( self.m_mainWindow.showReportManager )
        #self.connect( reportManagerAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('showReportManager()'))

        createReportAct = QAction( self.tr("新建"), reportMenu)
        reportMenu.addAction( createReportAct)
        self.connect( createReportAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('createReport()'))

        reportEditAct = QAction( self.tr("编辑"), reportMenu)
        reportMenu.addAction( reportEditAct)
        self.connect( reportEditAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('reportEdit()'))

        reportUploadAct = QAction( self.tr("入库"), reportMenu)
        reportMenu.addAction( reportUploadAct)
        reportUploadAct.triggered.connect( self.m_mainWindow.reportUpload)

        reportDownloadAct = QAction( self.tr("下载"), reportMenu)
        reportMenu.addAction( reportDownloadAct)
        reportDownloadAct.triggered.connect( self.m_mainWindow.reportDownload)
        
        """菜单-任务
        """
        taskMenu = self.m_menuBar.addMenu( self.tr("任务"))
        selectTaskAct = QAction( self.tr("选择任务"), taskMenu)
        taskMenu.addAction( selectTaskAct)
        selectTaskAct.triggered.connect( self.m_mainWindow.selectTask)
       
        updateTaskAct = QAction( self.tr("更新任务数据"), taskMenu)
        taskMenu.addAction( updateTaskAct)
        self.connect( updateTaskAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('updateTask()'))

        """菜单-关于
        """
        aboutMenu = self.m_menuBar.addMenu( self.tr("关于"))
        aboutAct = QAction( self.tr("关于"), aboutMenu)
        aboutMenu.addAction( aboutAct)
        aboutAct.triggered.connect( self.m_mainWindow.about)
        





