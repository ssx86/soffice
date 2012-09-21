#coding=utf-8

import sys
import os
import subprocess
import time

#os.environ['URE_BOOTSTRAP'] = 'vnd.sun.star.pathname:c:\Program Files\OpenOffice.org 3\program\fundamental.ini'
os.environ['URE_BOOTSTRAP'] = 'vnd.sun.star.pathname:/opt/openoffice.org3/program/fundamentalrc'
#os.environ['UNO_PATH'] = 'c:\Program Files\OpenOffice.org 3\program\\'
#os.environ['PATH'].append('c:\Program Files\OpenOffice.org 3\URE\bin;c:\Program Files\OpenOffice.org 3\Basis\program;')

sys.path.append( r'C:\Program Files\OpenOffice.org 3\Basis\program')
sys.path.append( r'C:\Program Files\OpenOffice.org 3\program')

import socket
import uno
import unohelper
from officehelper import *
from com.sun.star.text.ControlCharacter import PARAGRAPH_BREAK 
class OoEngine():

    def __init__( self):
        print "OoEngine __init__"
        self.m_context = None

#    @staticmethod
    def getInstance( self):
        print "OoEngine getInstance"

#    @staticmethod
    def startupDesktop( self):
        print "OoEngine startupDesktop"

        localContext = uno.getComponentContext()

        resolver = localContext.ServiceManager.createInstanceWithContext( "com.sun.star.bridge.UnoUrlResolver", localContext )

        #connect 
        if self.m_context == None:
            print "first connect"
            self.m_context = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
        else:
            print "remained context"
        smgr = self.m_context.ServiceManager

        self.m_desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop", self.m_context)
        frame = self.m_desktop.getCurrentFrame()
        window = frame.getContainerWindow()
        window.setVisible( False)

        
#    @staticmethod
    def openDocument( self):
        print "OoEngine openDocument"
        
        self.m_doc = self.m_desktop.loadComponentFromURL( "private:factory/swriter", "_blank", 0, () )
        self.m_hasDoc = True
        

#    @staticmethod
    def insertText( self, _text):
        print "OoEngine insertText"
      
        text = self.m_doc.Text
        cursor = text.createTextCursor()
        text.insertString( cursor, _text, 0 )

    def insertTextIntoCell(self,  table, cellName, text, color ):
        print "OoEngine insertTextIntoCell"

        tableText = table.getCellByName( cellName)
        cursor = tableText.createTextCursor()
        cursor.setPropertyValue( "CharColor", color )
        tableText.setString( text )
    
    def insertTable( self, lstRowCol):
        print "OoEngine insertTable"

#        if ( self.m_hasDoc == False):
#            pass

        # 得到文档文本
        text = self.m_doc.Text
        # 创建一个文本表格 
        table = self.m_doc.createInstance( "com.sun.star.text.TextTable" )

        # 初始化大小
        table.initialize( 4,3)

        # 得到光标位置
        cursor = text.createTextCursor()
        # 插入表格
        text.insertTextContent( cursor, table, 0 )
        oldContext = uno.getCurrentContext()
        unohelper.CurrentContext( oldContext,{"My42":42})  
        oldContext = uno.getCurrentContext()

        # test 设置其中一个格的文本
        table.getCellByName("A3").setValue(55)
        self.insertTextIntoCell(table, "B2", "i am b2", 5734)

    def insert_index(self, text):
        print "insert index"
        _text = self.m_doc.Text
        cursor = _text.createTextCursor()
        cursor.gotoEnd(False)
        _text.insertString( cursor, text, 0 )
        _text.insertControlCharacter(cursor, PARAGRAPH_BREAK, False)
        _text.insertString( cursor, text, 0 )


