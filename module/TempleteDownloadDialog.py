#!/usr/bin/python
#coding=utf-8
# ģ�����ضԻ�����
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TempleteDownloadDialog( QDialog):
    def __init__( self, parent=None):
        super( TempleteDownloadDialog, self).__init__( parent)

        self.setupUI()
        print "TempleteDownloadDialog init.."
        
    def setupUI(self):
        print "TempleteDownloadDialog setupUI.."
        self.setWindowTitle( self.tr("ģ�����ضԻ���"))

        """�˵�-�ļ�
        """
        
        





