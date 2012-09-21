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
        templeteMenu = self.m_menuBar.addMenu( self.tr("ģ��"))
        createTempleteAct = QAction( self.tr("�½�"), templeteMenu)
        templeteMenu.addAction( createTempleteAct)
        self.connect( createTempleteAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('createTemplete()'))

        templeteEditAct = QAction( self.tr("�༭"), templeteMenu)
        templeteMenu.addAction( templeteEditAct)
        self.connect( templeteEditAct, SIGNAL('triggered(bool)'), self.m_mainWindow, SLOT('templeteEdit()'))

        templeteUploadAct = QAction( self.tr("���"), templeteMenu)
        templeteMenu.addAction( templeteUploadAct)
        templeteUploadAct.triggered.connect( self.m_mainWindow.templeteUpload)

        templeteDownloadAct = QAction( self.tr("����"), templeteMenu)
        templeteMenu.addAction( templeteDownloadAct)
        templeteDownloadAct.triggered.connect( self.m_mainWindow.templeteDownload)

        """�˵�-����
        """
        reportMenu = self.m_menuBar.addMenu( self.tr("����"))
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
        





