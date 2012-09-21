#!/usr/bin/python
#coding=utf-8
# 任务树浮动面版类
#
#

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TaskTreeDockWidget( QTreeView):
    def __init__( self, parent=None):
        super( TaskTreeDockWidget, self).__init__( parent)
        
        

        print "TaskTreeDockWidget init.."
    def setupUI( self):
        print "TaskTreeDockWidget setupUI.."

        self.setWindowTitle( self.tr("任务信息列表"))


    def updateData( self):
        print "TaskTreeDockWidget updatedata.."
