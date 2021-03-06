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
from TemplateDownloadDialog import TemplateDownloadDialog
from ContentEditWidget import ContentEditWidget

# lsp
from About import About
from ReportManager import ReportManager
from TemplateManager import TemplateManager

sys.path.append( 'OpenOffice')
from OpenOffice import OpenOffice

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

    def templateDownload( self, bCheck):
        print "mainWindow templateDownload..."
        dlg = TemplateDownloadDialog( self)
        dlg.exec_()

    def reportDownload( self, bCheck):
        print "mainWindow reportDownload..."
        dlg = ReportDownloadDialog( self)
        dlg.exec_()

    def about( self, bCheck):
        print "mainWindow about..."
        dlg = About(self)
        dlg.exec_()

    def showTemplateManager(self, bCheck):
        print "templatemanager menu"
        dlg = TemplateManager(self)
        dlg.exec_()

    def showReportManager(self, bCheck):
        print "reportmanager menu"
        dlg = ReportManager(self)
        dlg.exec_()
        
    def contentEdit( self, bCheck):
        print "mainWindow contentEdit..."
        editWid = ContentEditWidget( )
        self.setCentralWidget( editWid)
        editWid.show()

    def templateUpload( self, bCheck):
        print "mainWindow templateUpload..."
        filepath = QFileDialog.getOpenFileName( self)
        print ( "filepath is : %s", filepath)

    def reportUpload( self, bCheck):
        print "mainWindow reportUpload..."
        filepath = QFileDialog.getOpenFileName( self)
        print ( "filepath is : %s", filepath)

    def openDocument( self, bCheck):
        print "mainWindow openDocument..."
        
        office = OpenOffice("怎么回事儿.odt")

        # Insert some text
        office.setListFormat(QTextListFormat.ListUpperAlpha)

        office.insertImage("img/123.png", 50, 200, QTextFrameFormat.FloatRight)
        office.insertList()

        office.insertText("中文\n")
        office.insertText("two\n")
        office.insertText("three\n")
        office.insertText("\n")
        office.insertText("\n")
        office.insertText("\n")

        office.reset()

        #cursor.insertBlock()
        #
        #listFormat.clearProperty(QTextFormat.ListStyle)
        #
        #cursor.insertBlock()
        #
        #cursor.insertText("one")
        #cursor.insertText("\ntwo")
        #cursor.insertText("\nthree")


        office.setBlockBgColor(QColor(255, 0, 0))
        office.insertText("123")

        office.setBlockBgColor(QColor(255, 255, 0))
        office.insertText("456")

        office.setBlockBgColor(QColor(0, 255, 0))
        office.insertText("789\n101001 ")

        table = office.insertTable(10, 3)
        office.tableMergeCells(table, 2, 2, 4, 1)

        office.tableMoveToCell(table, 4, 1)

        office.insertText("asdfasdf")

        office.done()
