#!/usr/bin/python
#coding=utf-8
# ģ�����ضԻ�����
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TemplateDownloadDialog( QDialog):
    def __init__( self, parent=None):
        super( TemplateDownloadDialog, self).__init__( parent)

        self.setupUI()
        print "TemplateDownloadDialog init.."
        
    def setupUI(self):
        print "TemplateDownloadDialog setupUI.."
        self.setWindowTitle( self.tr("ģ�����ضԻ���"))

        """�˵�-�ļ�
        """
        
        





