#!/usr/bin/python
#coding=utf-8
# 报告生成工具主界面
#
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4 import Qt

from MenuMgr import MenuMgr
from ToolBarMgr import ToolBarMgr
from TaskTreeDockWidget import TaskTreeDockWidget

sys.path.append( 'module')
from TaskSelectDialog import TaskSelectDialog
from ReportDownloadDialog import ReportDownloadDialog
from TempleteDownloadDialog import TempleteDownloadDialog
from AboutDialog import AboutDialog
from ContentEditWidget import ContentEditWidget

sys.path.append( 'Ooo')
from OoEngine import OoEngine

class MainWindow( QMainWindow):
    def __init__( self, parent=None):
        super( MainWindow, self).__init__( parent)

        print "mainwindow init.."
        self.setCentralWidget( QWidget())
        self.setupUI()
        
        
    def setupUI( self):
        print "mainWindow setupUI.."
        QTextCodec.setCodecForTr(QTextCodec.codecForName("gbk"))
        self.setWindowTitle( self.tr("辅助报告生成工具"))
        self.setGeometry(10, 10, 1000, 500);
        self.setWindowIcon( QIcon( self.tr("./img/app.png")))
        MenuMgr( self).setupUI()
        ToolBarMgr( self).setupUI()

        self.setupDockWidget()
        self.setupStatuBar()

    def setupDockWidget( self):
        taskTreeDockWidget = QDockWidget( self.tr("任务信息列表"), self)
        taskTreeDockWidget.setWidget( TaskTreeDockWidget())
        self.addDockWidget( 0x1, taskTreeDockWidget)

    def setupStatuBar( self):
        statusBar = self.statusBar()

   
    """@PyQt4.QtCore.pyqtSlot(bool)"""
    """pyqtSlot(bool)"""
    def fileEdit( self, bCheck):
        print "mainWindow fileEdit.."
        
        

    def selectTask( self, bCheck):
        print "mainWindow selectTask..."
        dlg = TaskSelectDialog( self)
        dlg.exec_()

    def templeteDownload( self, bCheck):
        print "mainWindow templeteDownload..."
        dlg = TempleteDownloadDialog( self)
        dlg.exec_()

    def reportDownload( self, bCheck):
        print "mainWindow reportDownload..."
        dlg = ReportDownloadDialog( self)
        dlg.exec_()

    def about( self, bCheck):
        print "mainWindow about..."
        dlg = AboutDialog( self)
        dlg.exec_()
        
    def contentEdit( self, bCheck):
        print "mainWindow contentEdit..."
        editWid = ContentEditWidget( )
        self.setCentralWidget( editWid)
        editWid.show()

    def templeteUpload( self, bCheck):
        print "mainWindow templeteUpload..."
        filepath = QFileDialog.getOpenFileName( self)
        print ( "filepath is : %s", filepath)

    def reportUpload( self, bCheck):
        print "mainWindow reportUpload..."
        filepath = QFileDialog.getOpenFileName( self)
        print ( "filepath is : %s", filepath)

    def openDocument( self, bCheck):
        print "mainWindow openDocument..."
        
        oe = OoEngine()
#        oe.startupDesktop()
#        oe.openDocument()
#        oe.insertText( "hello...........")

        oe.startupDesktop()
        oe.openDocument()
        oe.insert_index('asdfasdfasdfasdf')

        lstRowCol = [['' for x in range(3)] for y in range(4)]
        lstRowCol[0][0] = '1'
        lstRowCol[0][1] = '2'
        lstRowCol[0][2] = '3'
        lstRowCol[1][0] = '4'
        lstRowCol[1][1] = '5'
        lstRowCol[1][2] = '6'
        lstRowCol[2][0] = '7'
        lstRowCol[2][1] = '8'
        lstRowCol[2][2] = '9'
        lstRowCol[3][0] = '10'
        lstRowCol[3][1] = '11'
        lstRowCol[3][2] = '12'
        
        oe.insertTable( lstRowCol)
