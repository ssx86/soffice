#!/usr/bin/python
#coding=utf-8
# ����ѡ��Ի�����
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TaskSelectDialog( QDialog):
    def __init__( self, parent=None):
        super( TaskSelectDialog, self).__init__( parent)

        self.setupUI()
        print "TaskSelectDialog init.."
        
    def setupUI(self):
        print "MenuMgr setupUI.."
        self.setWindowTitle( self.tr("����ѡ��Ի���"))

        """�˵�-�ļ�
        """
        
        





