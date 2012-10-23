# coding=UTF-8

from PyQt4 import QtCore
from PyQt4.QtCore import QObject
from PyQt4.QtCore import QTextCodec
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import QSize

from PyQt4 import QtGui
from PyQt4.QtGui import QTextDocument
from PyQt4.QtGui import QTextFrameFormat
from PyQt4.QtGui import QImage
from PyQt4.QtGui import QTextFormat
from PyQt4.QtGui import QTextCharFormat
from PyQt4.QtGui import QTextImageFormat
from PyQt4.QtGui import QTextListFormat
from PyQt4.QtGui import QTextBlockFormat
from PyQt4.QtGui import QColor


class OpenOffice(QObject):
    def __init__(self, outFileName):
        super(QObject, self).__init__()
        # 输出文件的文件名
        self.outFileName = self.tr(outFileName)

        # QTextDocument文件对象
        self.doc = QtGui.QTextDocument()

        # 文件光标
        self.cursor = QtGui.QTextCursor(self.doc)

        # -------初始化样式设置
        # 列表样式
        self.listFormat = QTextListFormat()
        self.listFormat.setStyle(QTextListFormat.ListUpperAlpha)

        # 块样式
        self.blockFormat = QTextBlockFormat()

    def done(self):
        writer = QtGui.QTextDocumentWriter()

        #writer.setCodec(QTextCodec.codecForName("utf-8"))
        #print writer.codec().name()

        print writer.supportedDocumentFormats()
        #[PyQt4.QtCore.QByteArray(b'HTML'), PyQt4.QtCore.QByteArray(b'ODF'), PyQt4.QtCore.QByteArray(b'plaintext')]
        odf_format = writer.supportedDocumentFormats()[1]

        writer.setFormat(odf_format)
        writer.setFileName(self.outFileName)
        writer.write(self.doc) # Return True if successful
        
    def setListFormat(self, style):
        #
        # 可用的风格有：
        # QTextListFormat.ListDisc   -1  a filled circle
        # QTextListFormat.ListCircle -2  an empty circle
        # QTextListFormat.ListSquare -3  a filled square
        # QTextListFormat.ListDecimal    -4  decimal values in ascending order
        # QTextListFormat.ListLowerAlpha -5  lower case Latin characters in alphabetical order
        # QTextListFormat.ListUpperAlpha -6  upper case Latin characters in alphabetical order
        # QTextListFormat.ListLowerRoman -7  lower case roman numerals (supports up to 4999 items only)
        # QTextListFormat.ListUpperRoman -8  upper case roman numerals (supports up to 4999 items only)
        #
        self.listFormat.setStyle(style)

    def setBlockBgColor(self, color):
        self.blockFormat.setBackground(color)
        self.cursor.insertBlock(self.blockFormat)

    def reset(self):
        self.cursor.insertBlock(self.blockFormat)

    def setFont(self, font):
        print "set font..."

    def insertText(self, text):
        self.cursor.insertText(self.tr(text))

    def insertList(self):
        self.cursor.insertList(self.listFormat)

    def insertTable(self, row, column):
        return self.cursor.insertTable(row, column)

    # table
    def tableMergeCells(self, table, x, y, row, column):
        return table.mergeCells(x, y, row, column)

    def tableMoveToCell(self, table, x, y):
        self.cursor = table.cellAt(x, y).firstCursorPosition()

    def insertImage(self, imagePath, x = 200, y = 200, pos = QTextFrameFormat.FloatLeft):
        #
        # QTextFrameFormat.InFlow  0
        # QTextFrameFormat.FloatLeft 1
        # QTextFrameFormat.FloatRight    2
        #
        img = QImage()
        ok = img.load(imagePath)
        self.doc.addResource(QTextDocument.ImageResource, QUrl("myimage"), img)

        imageFormat = QTextImageFormat()
        imageFormat.setName("myimage")
        imageFormat.setWidth(x)
        imageFormat.setHeight(y)
        self.cursor.insertImage(imageFormat, pos)


    def test(self):
        #QTextCharFormat char_fmt;
        char_fmt = QTextCharFormat()

        char_fmt.setBackground(QColor(150, 150, 250));
        self.cursor.insertText(self.tr("Ì1\n"),char_fmt);
        #QImage img;
        img = QImage()
        ok = img.load("./123.png")
        self.doc.addResource(QTextDocument.ImageResource, QUrl("myimage"), img)

        imageFormat = QTextImageFormat()
        imageFormat.setName("myimage")
        imageFormat.setWidth(10)
        imageFormat.setHeight(10)
        self.cursor.insertImage(imageFormat)

        #self.cursor.insertImage("myimage");
        self.cursor.insertText(self.tr("Æåñòêèé äèñê\n"),char_fmt);
