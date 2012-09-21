#!/usr/bin/python
#coding=utf-8
# 关于对话框类
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AboutDialog( QDialog):
    def __init__( self, parent=None):
        super( AboutDialog, self).__init__( parent)

        self.setupUI()
        print "AboutDialog init.."
        
    def setupUI(self):
        print "AboutDialog setupUI.."
        self.setWindowTitle( self.tr("关于"))

        """菜单-文件
        """
        
        





