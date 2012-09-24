#coding=utf-8


import os
import sys
import getopt

sys.path.append("/opt/openoffice.org3.0/program/")
#os.environ['URE_BOOTSTRAP'] = 'vnd.sun.star.pathname:c:\Program Files\OpenOffice.org 3\program\fundamental.ini'
os.environ['URE_BOOTSTRAP'] = 'vnd.sun.star.pathname:/opt/openoffice.org3/program/fundamentalrc'
#os.environ['UNO_PATH'] = 'c:\Program Files\OpenOffice.org 3\program\\'
#os.environ['PATH'].append('c:\Program Files\OpenOffice.org 3\URE\bin;c:\Program Files\OpenOffice.org 3\Basis\program;')



import uno

from unohelper import Base, absolutize, systemPathToFileUrl
from com.sun.star.io import XOutputStream, IOException
from com.sun.star.beans import PropertyValue
#from com.sun.star.text import XTextFieldsSupplier, XBookmarksSupplier   # interfaces
# values for the property "UpdateDocMode"
from com.sun.star.document.UpdateDocMode import NO_UPDATE, QUIET_UPDATE, ACCORDING_TO_CONFIG, FULL_UPDATE
# value for the property "MacroExecMode"
from com.sun.star.document.MacroExecMode import NEVER_EXECUTE, FROM_LIST, ALWAYS_EXECUTE, USE_CONFIG, ALWAYS_EXECUTE_NO_WARN, USE_CONFIG_REJECT_CONFIRMATION, USE_CONFIG_APPROVE_CONFIRMATION, FROM_LIST_NO_WARN, FROM_LIST_AND_SIGNED_WARN, FROM_LIST_AND_SIGNED_NO_WARN
from com.sun.star.uno import Exception as UnoException
from com.sun.star.connection import NoConnectException
from com.sun.star.lang import IllegalArgumentException

from com.sun.star.style.BreakType import PAGE_BEFORE, PAGE_AFTER, NONE, PAGE_BOTH

sys.path.append("../utils")
from file_system import FileSystem

fs = FileSystem(".")

class OoAccess(object):
    def __init__(self, ooPort=2002, fileSystem=None):
        if fileSystem is None:
            self.__fs = fs
        else:
            self.__fs = fileSystem
        connectString = "uno:socket,host=localhost,port=%s;urp;StarOffice.ComponentContext"
        connectString = connectString % ooPort
        try:
            # get the uno component context from the PyUNO runtime
            self.localContext = uno.getComponentContext()
            # create UnoUrlResolver
            self.resolver = self.localContext.ServiceManager.createInstanceWithContext(
                "com.sun.star.bridge.UnoUrlResolver", self.localContext)
            # connect to the running office
            self.ctx = self.resolver.resolve(connectString)
            self.smgr = self.ctx.ServiceManager
            # get the centrol desktop object
            self.desktop = self.smgr.createInstanceWithContext("com.sun.star.frame.Desktop", self.ctx)
        except NoConnectException, e:
            raise Exception("OpenOffice process not found or not listening (%s)" % str(e))
        except IllegalArgumentException, e:
            raise Exception("The url is invalid (%s)" % str(e))
        except RuntimeException, e:
            raise Exception("An unknown error occured: %s" % str(e))
    
    
    def __del__(self):
        # In case the last call is a oneway call, it must be forced out of the remote-bridge
        # caches before python exits the process.  Otherwise, the oneway call may or may not 
        # reach the target object.
        # It is done here with a cheap synchronous call (getPropertyValue).
        self.ctx.ServiceManager
        
    def __getModel(self):
        # access the current writer document
        model = self.desktop.getCurrentComponent()
        return model
    model = property(__getModel)    
    
    
    def test(self, msg="Hello World ", capture=False):
        # access the document's text property

        # text = self.model.Text()
        text = self.desktop.loadComponentFromURL( "private:factory/swriter", "_blank", 0, () ).Text
        # create a cursor
        cursor = text.createTextCursor()
        # insert the text into the document
        text.insertString(cursor, msg, capture)
    
    def createDispatchHelper(self):
        dispatchHelper = "com.sun.star.frame.DispatchHelper"
        #dispatcher = self.smgr.createInstance(dispatchHelper)
        # or
        dispatcher = self.smgr.createInstanceWithContext(dispatchHelper, self.ctx)
        return dispatcher

    def addBookmark(self, doc, cursor, bookmarkName):
        bookmark = doc.createInstance("com.sun.star.text.Bookmark")
        bookmark.Name = bookmarkName
        doc.Text.insertTextContent(cursor, bookmark, True)

    # draft
    def deleteBookmark(self, doc, bookmarkName):
        #dipatcher = self.createDispatchHelper()
        #frame = doc.getCurrentController().getFrame()
        #prop = PropertyValue()
        #prop.Name = "Bookmark"
        #prop.Value = bookmarkName
        #props = (prop, )
        #dispatcher.executeDispatch(frame, ".uno:DeleteBookmark", "", 0, props)
        ## (frame, ".uno:StateBookmark", "", 0, tuple())
        bookmarks = doc.getBookmarks()
        if bookmarks.hasByName(bookmarkName):
            bookmark = bookmarks.getByName(bookmarkName)
            bookmark.dispose()
    
    def getCursorForBookmark(self, doc, bookmarkName):
        bookmarks = doc.getBookmarks()
        if bookmarks.hasByName(bookmarkName):
            bookmark = bookmarks.getByName(bookmarkName)
            r = bookmark.getAnchor()
            cursor = r.Text.createTextCursorByRange(r)
            return cursor
        else:
            return None

    def getViewCursor(self, doc=None):
        if doc==None:
            doc = self.model
        cursor = doc.getCurrentContoller().getViewCursor()
        return cursor

    # draft
    def updateIndex(self, doc):
        dispatcher = self.createDispatchHelper()
        frame = doc.getCurrentController().getFrame()
        dispatcher.executeDispatch(frame, ".uno:UpdateCurIndex", "", 0, tuple())

    def updateAll(self, doc=None):
        if doc is None:
            doc = self.model
        frame = doc.getCurrentController().getFrame()
        dispatcher = self.createDispatchHelper()
        dispatcher.executeDispatch(frame, ".uno:UpdateAll", "", 0, ())

    def regexSearch(self, doc, pattern, replace):
        search = doc.crateSearchDescriptor()
        search.SearchRegularExpression = True
        search.SearchString = pattern
        found = doc.findFirst(search)   # findNext(), findAll()
        cursor = found.Text.createCursorByRange(found)
        cursor.String = replace

    def getNewDocument(self):
        inProps = tuple()
        #inProps = self.__getInProperties()
        # for a Bibliography factory use ".component:Bibliography/View1"
        # Target Frame = "_blank" -> Creates a new top-level frame as a child frame of the desktop
        newdoc = self.desktop.loadComponentFromURL("private:factory/swriter", "_blank", 0, inProps)
        #text = newdoc.Text
        #cursor = text.createTextCursor()
        return newdoc
    
    def saveDoc(self, doc, toFile):
        filterName = "writer8"
        outputStream = OutputStream()       # Writes to sys.stdout
        outProps = self.__getOutProperties(filterName, outputStream)
        l = [("FilterName", 0, filterName, 0), ("Overwrite", 0, True, 0), \
                ("OutputStream", 0, outputStream, 0), \
                ("Unpacked", 0, True, 0)]
        outProps = self.getProps(l)
        toFileUrl = self.pathToUrl(toFile)
        doc.storeToURL(toFileUrl, outProps)
    
    def closeDoc(self, doc):
        doc.dispose()        
    
    def insertDocumentInto(self, doc, insertFile):
        insertFileUrl = self.pathToUrl(insertFile)
        text = doc.Text
        cursor = text.createTextCursor()
        try:
            cursor.gotoEnd(False)
            cursor.BreakType = PAGE_BEFORE
            cursor.insertDocumentFromURL(insertFileUrl, ())
        except IOException, e:
            raise Exception("Error during opening (%s)" % str(e))
        except IllegalArgumentException, e:
            raise Exception("The rul is invalid (%s)" % str(e))
        except UnoException, e:
            raise Exception("Error (%s) during conversion: %s" % (e.__class__, str(e)))

    def insertDocumentAtCursor(self, cursor, insertFile):
        insertFileUrl = self.pathToUrl(inserFile)
        cursor.insertDocumentFromURL(insertFileUrl, ())

    
    def loadDocument(self, fromFile, visible=False):
        doc = None
        fromFileUrl = self.pathToUrl(fromFile)
        inProps = self.__getInProperties()
        if visible:
            inProps = inProps[1:]
        try:
            doc = self.desktop.loadComponentFromURL(fromFileUrl, "_blank", 0, inProps)
        except IOException, e:
            msg = str(e)
            raise
        except UnoException, e:
            msg = str(e)
            raise
        return doc


    def convert(self, fromFile, toFile=None, toExt=None):
        if toExt is None or not(toExt.startswith(".")):
            if toFile is not None:
                #toExt = os.path.splitext(toFile)[1]
                toExt = self.__fs.splitExt(toFile)[1]
            else:
                toExt = ".txt"
        fromFileUrl = self.pathToUrl(fromFile)
        if toFile is None:
            toFileUrl = "private:stream"
        else:
            toFileUrl = self.pathToUrl(toFile)
        filterName, msg = self.__getFliterName(toExt)
        result, messages = self.__convert(fromFileUrl, toFileUrl, filterName)
        messages.insert(0, msg)
        return result, messages


    def __convert(self, fromFileUrl, toFileUrl, filterName):
        result = False
        doc = None
        messages = []
        outputStream = OutputStream()       # Writes to sys.stdout
        inProps = self.__getInProperties()
        outProps = self.__getOutProperties(filterName, outputStream)
        try:
            try:
                # fromUrl = "private:factory/swriter"  # to create a new odt document
                #                            (fromUrl, targetFrameName, SearchFlags, inProps)
                doc = self.desktop.loadComponentFromURL(fromFileUrl, "_blank", 0, inProps)
                if not(doc):
                    raise UnoException("Couldn't open input steam for an unknown reason", None)
                messages.append("Loaded Document OK")
                # save to document
                doc.storeAsURL(toFileUrl, outProps)
                #doc.storeToURL("private:stream", outProps)     # outputStream (stdout)
                messages.append("Converted OK")
                result = True
            except IOException, e:
                msg = str(e)
                messages.append("ERROR: IO Error during conversion: %s" % msg)
            except UnoException, e:
                msg = str(e)
                messages.append("ERROR: Error(%s) during conversion: %s" % (e.__class__, msg))
        finally:
            if not(doc):
                doc.dispose()
                doc = None
        outputStream.flush()    
        return result, messages
    
    
    def getProps(self, properties=[]):
        props = []
        for name, x, value, y in properties:
            prop = PropertyValue(name, x, value, y)
            props.append(prop)
        return tuple(props)
    
    
    def pathToUrl(self, path):
        #url = systemPathToFileUrl(os.path.abspath(path))
        url = systemPathToFileUrl(self.__fs.absPath(path))
        return url

    def __getInProperties(self):
        # "AsTemplate" = True|False
        # "JumpMark" = bookmarkName
        # "DocumentBaseURL" = The base URL of the document to be used to resolve relative links
        # "DocumentTitle" = "Title"
        # "FilterName", "FilterOptions", "FilterData"
        # "InteractionHandler" = com.sun.star.task.XInteractionHandler
        # "Password"
        # "RepairPackage" = True
        # "TemplateName" or "TemplateRegionName"
        # "URL" = "url of the document"
        # "MacroExecutionMode" = ALWAYS_EXECUTE_NO_WARN(=4)  MacroExecMode.Xxx constant list
        l = [   ("Hidden", 0, True, 0), \
                ("UpdateDocMode", 0, QUIET_UPDATE, 0), \
                ("MacroExecutionMode", 0, ALWAYS_EXECUTE_NO_WARN, 0), \
            ]
        return self.getProps(l)   
    
    def __getOutProperties(self, filterName, outputStream):
        # "Unpacked" = True
        l = [("FilterName", 0, filterName, 0), ("Overwrite", 0, True, 0), \
                ("OutputStream", 0, outputStream, 0)]
        return self.getProps(l)
    
    
    def __getFliterName(self, toExt):
        msg = ""
        if toExt == ".htm" or toExt==".html" or toExt=="":
            filterName = "HTML (StarWriter)"
            msg = "convertToHtml"
        elif toExt == ".doc":
            filterName = "MS Word 97"
            msg = "convertToWordDoc"
        elif toExt == ".odt":
            filterName = "writer8"
            msg = "convertToOdt"
        elif toExt == ".sxw":
            filterName = "StarOffice XML (Writer)"
            msg = "convertToSxw"
        elif toExt == ".pdf":
            filterName = "writer_pdf_Export"
            msg = "convertToPdf"
        elif toExt == ".txt":
            filterName = "Text (Encoded)"
            msg = "convertToText"
        else:
            raise Exception("unsupport extension type! ext=", toExt)
        return filterName, msg





class OutputStream(Base, XOutputStream):
    def __init__(self):
        self.closed=0
    def closeOutput(self):
        self.closed = 1
    def writeBytes(self, seq):
        sys.stdout.write(seq.value)
    def flush(self):
        sys.stdout.flush()


class OoObject(object):
    def __init__(self, ooPort=2002):
        connectString = "uno:socket,host=localhost,port=%s;urp;StarOffice.ComponentContext"
        connectString = connectString % ooPort
        desktop = "com.sun.star.frame.Desktop"
        try:
            # get the uno component context from the PyUNO runtime
            self.__localContext = uno.getComponentContext()
            # create UnoUrlResolver
            self.__resolver = self.__localContext.ServiceManager.createInstanceWithContext(
                "com.sun.star.bridge.UnoUrlResolver", self.__localContext)
            # connect to the running office
            self.__ctx = self.__resolver.resolve(connectString)
            self.__smgr = self.__ctx.ServiceManager
            # get the centrol desktop object
            self.__desktop = self.__smgr.createInstanceWithContext(desktop, self.__ctx)
        except NoConnectException, e:
            raise Exception("OpenOffice process not found or not listening (%s)" % str(e))
        except IllegalArgumentException, e:
            raise Exception("The url is invalid (%s)" % str(e))
        except RuntimeException, e:
            raise Exception("An unknown error occured: %s" % str(e))
        self.__doc = self.__desktop.getCurrentComponent()
        self.__text = None
        self.__cursor = None
        self.__viewCursor = None
        self.__search = None
        try:
            self.__text = self.__doc.Text
            self.__cursor = self.__text.createTextCursor()
        except:
            pass    
    
    def __del__(self):
        # In case the last call is a oneway call, it must be forced out of the remote-bridge
        # caches before python exits the process.  Otherwise, the oneway call may or may not 
        # reach the target object.
        # It is done here with a cheap synchronous call (getPropertyValue).
        self.__ctx.ServiceManager
    

    def setDoc(self, doc):
        self.__doc = doc
        self.__text = self.__doc.Text
        self.__cursor = self.__text.createTextCursor()
        self.__viewCursor = None
        self.__search = None
    def getDoc(self):
        return self.__doc
    doc = property(getDoc)

    def getText(self):
        return self.__text
    text = property(getText)

    def __getCursor(self):
        return self.__cursor
    def __setCursor(self, cursor):
        self.__cursor = cursor
    cursor = property(__getCursor, __setCursor)

    def __getViewCursor(self):
        if self.__viewCursor is None:
            vc = self.__doc.getCurrentController().getViewCursor()
            self.__viewCursor = vc
        return self.__viewCursor
    viewCursor = property(__getViewCursor)
    

    def __getCursorString(self):
        return self.__cursor.String
    def __setCursorString(self, value):
        self.__cursor.String = value;
    cursorString = property(__getCursorString, __setCursorString)
    

    def getTextString(self):
        return self.__text.String
    

    def getWordCount(self):
        return self.__doc.WordCount

    def getParagraphCount(self):
        return self.__doc.ParagraphCount

    def updateLinks(self):
        self.__doc.updateLinks()

    def reformat(self):
        self.__doc.reformat()


    def addText(self, text="-Hello World-", capture=False):
        # insert the text into the document
        msg = ""
        self.__text.insertString(self.__cursor, msg, capture)
    
    
    def getLastText(self, count=1):
        self.__cursor.gotoEnd(False)
        self.__cursor.goLeft(count, True)
        r = self.__cursor.String
        self.__cursor.gotoEnd(False)
        return r

    def createEnumeration(self):
        return self.__text.createEnumeration()

    # Cursor control
    def gotoEnd(self, capture=False):
        self.__cursor.gotoEnd(capture)

    def gotoStart(self, capture=False):
        self.__cursor.gotoStart(capture)

    def goLeft(self, count=1, capture=False):
        self.__cursor.goLeft(count, capture)

    def goRight(self, count=1, capture=False):
        self.__cursor.goRight(count, capture)

    def createCursorContentEnumeration(self):
        return self.__cursor.createContentEnumeration()

    def gotoRange(self, cursor, capture=False):
        self.__cursor.gotoRange(cursor, capture)
    def collapseToEnd(self):
        self.__cursor.collapseToEnd()
    def collapseToStart(self):
        self.__cursor.collapseToStart()
    def isCursorCollapsed(self):
        return self.__cursor.isCollapsed()

    # word
    def gotoEndOfWord(self, capture=False):
        self.__cursor.gotoEndOfWord(capture)
    def gotoStartOfWord(self, capture=False):
        self.__cursor.gotoStartOfWord(capture)
    def gotoNextWord(self, capture=False):
        self.__cursor.gotoNextWord(capture)
    def gotoPreviousWord(self, capture=False):
        self.__cursor.gotoPreviousWord(capture)
    def isEndOfWord(self):
        return self.__cursor.isEndOfWord()
    def isStartOfWord(self):
        return self.__cursor.isStartOfWord()
    # sentence
    def gotoEndOfSentence(self, capture=False):
        self.__cursor.gotoEndOfSentence(capture)
    def gotoStartOfSentence(self, capture=False):
        self.__cursor.gotoStartOfSentence(capture)
    def gotoNextSentence(self, capture=False):
        self.__cursor.gotoNextSentence(capture)
    def gotoPreviousSentence(self, capture=False):
        self.__cursor.gotoPreviousSentence(capture)
    def isEndOfSentence(self):
        return self.__cursor.isEndOfSentence()
    def isStartOfSentence(self):
        return self.__cursor.isStartOfSentence()
    # paragraph
    def gotoEndOfParagraph(self, capture=False):
        self.__cursor.gotoEndOfParagraph(capture)
    def gotoStartOfParagraph(self, capture=False):
        self.__cursor.gotoStartOfParagraph(capture)
    def gotoNextParagraph(self, capture=False):
        self.__cursor.gotoNextParagraph(capture)
    def gotoPreviousParagraph(self, capture=False):
        self.__cursor.gotoPreviousParagraph(capture)
    def isEndOfParagraph(self):
        return self.__cursor.isEndOfParagraph()
    def isStartOfParagraph(self):
        return self.__cursor.isStartOfParagraph()


    def addBookmark(self, bookmarkName):
        bookmark = doc.createInstance("com.sun.star.text.Bookmark")
        bookmark.Name = bookmarkName
        self.__text.insertTextContent(self.__cursor, bookmark, True)
    

    def deleteBookmark(self, bookmarkName):
        bookmarks = self.__doc.getBookmarks()
        if bookmarks.hasByName(bookmarkName):
            bookmark = bookmarks.getByName(bookmarkName)
            bookmark.dispose()
    
    
    def getCursorForBookmark(self, bookmarkName):
        bookmarks = doc.getBookmarks()
        if bookmarks.hasByName(bookmarkName):
            bookmark = bookmarks.getByName(bookmarkName)
            r = bookmark.getAnchor()
            self.Cursor = r.Text.createTextCursorByRange(r)
            return True
        else:
            return False
    

    # draft
    def insertPageBreak(self):
        # Note: uses the viewCursor
        # set the viewCursor to point at the same location (or range) as the cursor
        self.viewCursor.gotoRange(self.__cursor, False) 

        dispatcher = self.__createDispatchHelper()
        frame = self.__doc.getCurrentController().getFrame()
        props = ( PropertyValue("Kind", 0, 3, 0),
                    PropertyValue("TemplateName", 0, "", 0),
                    PropertyValue("PageNumber", 0, 0, 0)
                )
        dispatcher.executeDispatch(frame, ".uno:InsertBreak", "", 0, props)
        #self.gotoEnd(False)

    # draft
    def updateCursorIndex(self):
        # using the view cursor I guess?
        self.viewCursor.gotoRange(self.__cursor, False) 

        dispatcher = self.__createDispatchHelper()
        frame = self.__doc.getCurrentController().getFrame()
        dispatcher.executeDispatch(frame, ".uno:UpdateCurIndex", "", 0, tuple())
    

    def updateAllIndexs(self):
        frame = self.__doc.getCurrentController().getFrame()
        dispatcher = self.__createDispatchHelper()
        dispatcher.executeDispatch(frame, ".uno:UpdateAll", "", 0, ())
    

    def regexSearch(self, pattern):
        search = self.__doc.crateSearchDescriptor()
        search.SearchRegularExpression = True
        search.SearchString = pattern
        self.__search = search
        found = self.__doc.findFirst(search)   # findNext(), findAll()
        if found:
            self.Cursor = found.Text.createCursorByRange(found)
            return True
        else:
            return False
    

    def findNext(self):
        found = self.__doc.findNext(self.__search)
        if found:
            self.Cursor = found.Text.createCursorByRange(found)
            return True
        else:
            return False
    
            
    def regexSearchAndReplaceAll(self, pattern, replacementText):
        search = self.__doc.crateSearchDescriptor()
        search.SearchRegularExpression = True
        search.SearchString = pattern
        matches = self.__doc.findAll(search)
        for found in matches:
            cursor = found.Text.createCursorByRange(found)
            cursor.String = replace    
    

    def createNewDocument(self, visible=False):
        inProps = tuple()
        #inProps = self.__getInProperties()
        # for a Bibliography factory use ".component:Bibliography/View1"
        # Target Frame = "_blank" -> Creates a new top-level frame as a child frame of the desktop
        l = [ ("MacroExecutionMode", 0, ALWAYS_EXECUTE_NO_WARN, 0) ]
        if visible==False:
            l.append( ("Hidden", 0, True, 0) )
        inProps = self.__getProps(l)   
        doc = self.__desktop.loadComponentFromURL("private:factory/swriter", "_blank", 0, inProps)
        self.setDoc(doc)
    
    
    def loadDocument(self, fromFile, visible=False):
        doc = None
        fromFileUrl = self.__pathToUrl(fromFile)
        inProps = self.__getInProperties()
        if visible:
            inProps = inProps[1:]
        try:
            doc = self.__desktop.loadComponentFromURL(fromFileUrl, "_blank", 0, inProps)
            if not(doc):
                raise UnoException(
                    "Couldn't open input steam '%s' for an unknown reason" % fromFileUrl, None)
        except IOException, e:
            msg = str(e)
            raise Exception("ERROR: IO Error during conversion: %s" % msg)
        except UnoException, e:
            msg = str(e)
            raise Exception("ERROR: Error(%s) during loading: %s" % (e.__class__, msg))
        self.setDoc(doc)
        return True
    

    def saveDocument(self, toFile, toExt=None):
        result = False
        if toExt is None or not(toExt.startswith(".")):
            if toFile is not None:
                #toExt = os.path.splitext(toFile)[1]
                toExt = self.__fs.splitExt(toFile)[1]
            else:
                toExt = ".htm"
        if toFile is None:
            toFileUrl = "private:stream"
        else:
            toFileUrl = self.__pathToUrl(toFile)
        filterName, filterMsg = self.__getFliterName(toExt)
        outputStream = OutputStream()       # Writes to sys.stdout
        outProps = self.__getOutProperties(filterName, outputStream)
        if False:
            l = [   ("FilterName", 0, filterName, 0), ("Overwrite", 0, True, 0), \
                    ("OutputStream", 0, outputStream, 0), \
                    ("Unpacked", 0, True, 0), \
                ]
            outProps = self.__getProps(l)
        toFileUrl = self.__pathToUrl(toFile)
        try:
            try:
                self.__doc.storeToURL(toFileUrl, outProps)
                result = True
            except IOException, e:
                msg = str(e)
                raise Exception("ERROR: IO Error during conversion: %s" % msg)
            except UnoException, e:
                msg = str(e)
                raise Exception("ERROR: Error(%s) during saving: %s" % (e.__class__, msg))
        finally:
            outputStream.flush()    
        return result, filterMsg
    
    
    def insertDocument(self, insertDocFile):
        insertFileUrl = self.__pathToUrl(insertDocFile)
        try:
            self.__cursor.BreakType = PAGE_BEFORE     #PAGE_BEFORE, NONE
            self.__cursor.insertDocumentFromURL(insertFileUrl, ())
        except IOException, e:
            raise Exception("Error during opening (%s)" % str(e))
        except IllegalArgumentException, e:
            raise Exception("The rul is invalid (%s)" % str(e))
        except UnoException, e:
            raise Exception("Error (%s) during conversion: %s" % (e.__class__, str(e)))


    def convert(self, fromFile, toFile=None, toExt=None):
        messages = []
        result = False
        try:
            result = self.loadDocument(fromFile)
        except Exception, e:
            messages.append(str(e))
        if result==True:
            messages.append("Loaded Document OK")
            try:
                result, filterMsg = self.saveDocument(toFile, toExt)
                #messages.append(filterMsg)
                messages.append("Converted OK")
            except Exception, e:
                result = False
        return result, messages

    
    def close(self):
        self.__viewCursor = None
        self.__cursor = None
        self.__text = None
        self.__doc.close(True)
        #self.__doc.dispose()
        self.__doc = None

    def enumerateAllLinksInCursorRange(self):
        for elem in self.__enum(self.__cursor):
            for subElem in self.__enum(elem):
                if subElem.HyperLinkURL != "":
                    yield subElem


    def __createDispatchHelper(self):
        dispatchHelper = "com.sun.star.frame.DispatchHelper"
        #dispatcher = self.__smgr.createInstance(dispatchHelper)
        # or
        dispatcher = self.__smgr.createInstanceWithContext(dispatchHelper, self.__ctx)
        return dispatcher


    def __getProps(self, properties=[]):
        props = []
        for name, x, value, y in properties:
            prop = PropertyValue(name, x, value, y)
            props.append(prop)
        return tuple(props)

    
    def propertyValue(self, name, value):
        return PropertyValue(name, 0, value, 0)


    def __enum(self, obj):
        enum = obj.createEnumeration()
        while enum.hasMoreElements():
            yield enum.nextElement()

    def __pathToUrl(self, path):
        #url = systemPathToFileUrl(os.path.abspath(path))
        url = systemPathToFileUrl(self.__fs.absPath(path))
        return url


    def __getInProperties(self):
        # "AsTemplate" = True|False
        # "JumpMark" = bookmarkName
        # "DocumentBaseURL" = The base URL of the document to be used to resolve relative links
        # "DocumentTitle" = "Title"
        # "FilterName", "FilterOptions", "FilterData"
        # "InteractionHandler" = com.sun.star.task.XInteractionHandler
        # "Password"
        # "RepairPackage" = True
        # "TemplateName" or "TemplateRegionName"
        # "URL" = "url of the document"
        # "MacroExecutionMode" = ALWAYS_EXECUTE_NO_WARN(=4)  MacroExecMode.Xxx constant list
        l = [   ("Hidden", 0, True, 0), \
                ("UpdateDocMode", 0, QUIET_UPDATE, 0), \
                ("MacroExecutionMode", 0, ALWAYS_EXECUTE_NO_WARN, 0), \
            ]
        return self.__getProps(l)   

    
    def __getOutProperties(self, filterName, outputStream):
        # "Unpacked" = True
        l = [("FilterName", 0, filterName, 0), ("Overwrite", 0, True, 0), \
                ("OutputStream", 0, outputStream, 0)]
        return self.__getProps(l)
    
    
    def __getFliterName(self, toExt):
        msg = ""
        if toExt == ".htm" or toExt==".html" or toExt=="":
            filterName = "HTML (StarWriter)"
            msg = "ToHtml"
        elif toExt == ".doc":
            filterName = "MS Word 97"
            msg = "ToWordDoc"
        elif toExt == ".odt":
            filterName = "writer8"
            msg = "ToOdt"
        elif toExt == ".sxw":
            filterName = "StarOffice XML (Writer)"
            msg = "ToSxw"
        elif toExt == ".pdf":
            filterName = "writer_pdf_Export"
            msg = "ToPdf"
        elif toExt == ".txt":
            filterName = "Text (Encoded)"
            msg = "ToText"
        else:
            raise Exception("unsupport extension type! ext=", toExt)
        return filterName, msg
        

#a = OoAccess()
o = OoObject()

# Property (Props)
#   "JumpMark", "BookmarkName"  (inProps)
#   "Unpacked", True            (outProps)

# Notes:
#   If we want to access the current page number (or work with automatic page breaks) we must 
#       use the view cursor (and not the model cursor)

# Cursor object   Note: a cursor is a text range also
#   BreakType
#   PropertyXxxx
#   Start, End
#   String
#   Text
#   TextField
#   TextFrame
#   TextSection
#   Types
#   createContentEnumeration
#   #Note: bExpand=T|F to expand the cursor or not
#   gotoEnd(bExpand)
#   gotoRange(range, bExpand)
#   gotoStart(bExpand)
#   goRight/goLeft(count, bExpand)
#   gotoEndOfParagraph, gotoEndOfSentence, gotoPreviousWord
#   collapseToEnd() collapseToStart()
#   isCollapsed() - return False if this is a text range or True if not
#   hasElments()
#   insertDocumentFromURL(fileUrl, ())
#   get/setPropertyValue
#
#   HyperLinkEvents, HyperLinkName, HyperLinkTarget, HyperLinkURL
#  cursor.Text.instertString(cursor, string, bExpand)  bExpand=False

# Text
#   Start, End
#   String
#   Text
#   Types
#   createTextCursor()
#   createTextCursorByRange(range)
#   createEnumeration()
#   insetString(cursor, textStr, 0)
#   insertTextContent()
#   insertTextContentBefore/After()
#   removeTextContentBefore/After()
#   removeTextContent()

# Document (doc)
#   WordCount
#   ParagraphCount
#   Bookmarks
#   DocumentIndexes
#   EmbeddedObjects
#   EndnoteSettings
#   Endnotes
#   FootnoteSettings
#   Footnotes
#   GraphicObjects
#   Links   # link targets (types)
#   NumberFormatSettings
#   NumberFormats
#   Text
#   TextFields, TextFrames, TextSections, TextTables
#   Close
#   createInstance
#   createInstanceWithArguments
#   createLibrary
#   createReplaceDescriptor
#   createSearchDescriptor
#   dispose
#   findAll, findFirst, findNext
#   getDocumentInfo
#   getPropertyDefault, getPropertySetInfo, getPropertyState, getPropertyStates, 'getPropertyValue
#   hasLocation
#   reformat
#   render
#   replaceAll
#   updateLinks

