#!/usr/bin/python
#coding=utf-8
# �˵�������
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

        """�˵�-�ļ�
        """
        fileMenu = self.m_menuBar.addMenu( self.tr("�ļ�"))
        openFileAct = QAction( self.tr("��"), fileMenu)
        fileMenu.addAction( openFileAct)
        self.connect( openFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('openFile()'))

        saveFileAct = QAction( self.tr("����"), fileMenu)
        fileMenu.addAction( saveFileAct)
        self.connect( saveFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('saveFile()'))

        saveAsFileAct = QAction( self.tr("���Ϊ"), fileMenu)
        fileMenu.addAction( saveAsFileAct)
        self.connect( saveAsFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('saveAsFile()'))


        previewFileAct = QAction( self.tr("Ԥ��"), fileMenu)
        fileMenu.addAction( previewFileAct)
        self.connect( previewFileAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('previewFile()'))

        """�˵�-�༭
        """
        editMenu = self.m_menuBar.addMenu( self.tr("�༭"))
        fileEditAct = QAction( self.tr("�ļ��༭"), editMenu)
        editMenu.addAction( fileEditAct)
        fileEditAct.triggered.connect( self.m_mainWindow.fileEdit)

        setupAct = QAction( self.tr("���ĵ�"), editMenu)
        editMenu.addAction( setupAct)
        setupAct.triggered.connect( self.m_mainWindow.openDocument)

        contentEditAct = QAction( self.tr("���ݱ༭"), editMenu)
        editMenu.addAction( contentEditAct)
        contentEditAct.triggered.connect( self.m_mainWindow.contentEdit)

        """�˵�-ģ��
        """
        templateMenu = self.m_menuBar.addMenu( self.tr("ģ��"))
        templateManagerAct = QAction( self.tr("ģ�����"), templateMenu)
        templateMenu.addAction( templateManagerAct)
        templateManagerAct.triggered.connect( self.m_mainWindow.showTemplateManager )
        #self.connect( templateManagerAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('showTempleteManager()'))

        createTempleteAct = QAction( self.tr("�½�"), templateMenu)
        templateMenu.addAction( createTempleteAct)
        self.connect( createTempleteAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('createTemplete()'))

        templateEditAct = QAction( self.tr("�༭"), templateMenu)
        templateMenu.addAction( templateEditAct)
        self.connect( templateEditAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('templateEdit()'))

        templateUploadAct = QAction( self.tr("���"), templateMenu)
        templateMenu.addAction( templateUploadAct)
        templateUploadAct.triggered.connect( self.m_mainWindow.templateUpload)

        templateDownloadAct = QAction( self.tr("����"), templateMenu)
        templateMenu.addAction( templateDownloadAct)
        templateDownloadAct.triggered.connect( self.m_mainWindow.templateDownload)

        """�˵�-����
        """
        reportMenu = self.m_menuBar.addMenu( self.tr("����"))

        reportManagerAct = QAction( self.tr("�������"), reportMenu)
        reportMenu.addAction( reportManagerAct)
        reportManagerAct.triggered.connect( self.m_mainWindow.showReportManager )
        #self.connect( reportManagerAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('showReportManager()'))

        createReportAct = QAction( self.tr("�½�"), reportMenu)
        reportMenu.addAction( createReportAct)
        self.connect( createReportAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('createReport()'))

        reportEditAct = QAction( self.tr("�༭"), reportMenu)
        reportMenu.addAction( reportEditAct)
        self.connect( reportEditAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('reportEdit()'))

        reportUploadAct = QAction( self.tr("���"), reportMenu)
        reportMenu.addAction( reportUploadAct)
        reportUploadAct.triggered.connect( self.m_mainWindow.reportUpload)

        reportDownloadAct = QAction( self.tr("����"), reportMenu)
        reportMenu.addAction( reportDownloadAct)
        reportDownloadAct.triggered.connect( self.m_mainWindow.reportDownload)
        
        """�˵�-����
        """
        taskMenu = self.m_menuBar.addMenu( self.tr("����"))
        selectTaskAct = QAction( self.tr("ѡ������"), taskMenu)
        taskMenu.addAction( selectTaskAct)
        selectTaskAct.triggered.connect( self.m_mainWindow.selectTask)
       
        updateTaskAct = QAction( self.tr("������������"), taskMenu)
        taskMenu.addAction( updateTaskAct)
        self.connect( updateTaskAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('updateTask()'))

        """�˵�-����
        """
        aboutMenu = self.m_menuBar.addMenu( self.tr("����"))
        aboutAct = QAction( self.tr("����"), aboutMenu)
        aboutMenu.addAction( aboutAct)
        aboutAct.triggered.connect( self.m_mainWindow.about)
        





