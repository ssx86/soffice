#!/usr/bin/python
#coding=utf-8
# 报告生成工具主程序
#
#

import sys


from PyQt4.QtCore import *
from PyQt4.QtGui import *
#import ctypes
#ctypes.LibraryLoader( 'pyuno.dll')

#sys.path.append( r'C:\Program Files\OpenOffice.org 3\Basis\sdk\include\cppuhelper')

#from officehelper import BootstrapException

from MainWindow import MainWindow


def main():
    print "inter main.."
      
#    BootstrapException.bootstrap()

    app = QApplication( sys.argv)

    QTextCodec.setCodecForTr( QTextCodec.codecForLocale())
    QTextCodec.setCodecForCStrings( QTextCodec.codecForLocale())

    w = MainWindow()

    w.show()

   
    
    sys.exit( app.exec_())
    return 0

main()
