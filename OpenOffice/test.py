# coding:UTF-8

from OpenOffice import OpenOffice
from PyQt4.QtGui import QTextListFormat
from PyQt4.QtGui import QTextFrameFormat
from PyQt4.QtGui import QColor
from PyQt4.QtCore import QTextCodec

QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"))
QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"));
QTextCodec.setCodecForLocale(QTextCodec.codecForName("UTF-8"));

office = OpenOffice('走你.odt')

# Insert some text
office.setListFormat(QTextListFormat.ListUpperAlpha)

office.insertImage("./123.png", 50, 200, QTextFrameFormat.FloatRight)




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

