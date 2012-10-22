#coding:utf-8
from ooopy.Transformer import Transformer
from ooopy.OOoPy import OOoPy 


from PyQt4 import QtGui
from PyQt4.QtGui import QTextFormat
from PyQt4.QtGui import QTextListFormat
from PyQt4.QtGui import QTextBlockFormat
from PyQt4.QtGui import QColor

# Create a document object
doc = QtGui.QTextDocument()
# Create a cursor pointing to the beginning of the document
cursor = QtGui.QTextCursor(doc)

# Insert some text
listFormat = QTextListFormat()
listFormat.setStyle(QTextListFormat.ListDecimal)

cursor.insertList(listFormat)

cursor.insertText("one\n")
cursor.insertText("two\n")
cursor.insertText("three\n")

#cursor.insertBlock()
#
#listFormat.clearProperty(QTextFormat.ListStyle)
#
#cursor.insertBlock()
#
#cursor.insertText("one")
#cursor.insertText("\ntwo")
#cursor.insertText("\nthree")



format = QTextBlockFormat()
format.setBackground(QColor(255, 0, 0));
cursor.setBlockFormat(format);

cursor.insertText("the ");

format.setBackground(QColor(255, 255, 0));
cursor.insertBlock(format);
cursor.insertText("fish ");

format.setBackground(QColor(0, 0, 255));
cursor.insertBlock(format);
cursor.insertText("are ");

format.setBackground(QColor(0, 255, 255));
cursor.insertBlock(format);
cursor.insertText("coming!");


table = cursor.insertTable(10, 3)
table.mergeCells(2, 2, 4, 1)
cursor = table.cellAt(1, 1).firstCursorPosition();

cursor.insertBlock(format);
cursor.insertText("asdfasdf")


# Create a writer to save the document
writer = QtGui.QTextDocumentWriter()
writer.supportedDocumentFormats()
#[PyQt4.QtCore.QByteArray(b'HTML'), PyQt4.QtCore.QByteArray(b'ODF'), PyQt4.QtCore.QByteArray(b'plaintext')]
odf_format = writer.supportedDocumentFormats()[1]
writer.setFormat(odf_format)
writer.setFileName('hello_world.odt')
writer.write(doc) # Return True if successful
