#!/usr/bin/python
#coding=utf-8
# �������ضԻ�����
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ReportDownloadDialog( QDialog):
    def __init__( self, parent=None):
        super( ReportDownloadDialog, self).__init__( parent)

        self.setupUI()
        print "ReportDownloadDialog init.."
        
    def setupUI(self):
        print "ReportDownloadDialog setupUI.."
        self.setWindowTitle( self.tr("�������ضԻ���"))

        """�˵�-�ļ�
        """
        
        





