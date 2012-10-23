#!/usr/bin/python
#coding=utf-8
# xml文件读写的实验
#
#


#encoding:utf-8

from xml.dom.minidom import Document

attrs_document_content = {
    'xmlns:office'    : "urn:oasis:names:tc:opendocument:xmlns:office:1.0" ,
    'xmlns:style'     : "urn:oasis:names:tc:opendocument:xmlns:style:1.0" ,
    'xmlns:text'      : "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    'xmlns:table'     : "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    'xmlns:draw'      : "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    'xmlns:fo'        : "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    'xmlns:xlink'     : "http://www.w3.org/1999/xlink",
    'xmlns:dc'        : "http://purl.org/dc/elements/1.1/",
    'xmlns:meta'      : "urn:oasis:names:tc:opendocument:xmlns:meta:1.0",
    'xmlns:number'    : "urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0",
    'xmlns:svg'       : "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    'xmlns:chart'     : "urn:oasis:names:tc:opendocument:xmlns:chart:1.0",
    'xmlns:dr3d'      : "urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0",
    'xmlns:math'      : "http://www.w3.org/1998/Math/MathML",
    'xmlns:form'      : "urn:oasis:names:tc:opendocument:xmlns:form:1.0",
    'xmlns:script'    : "urn:oasis:names:tc:opendocument:xmlns:script:1.0",
    'xmlns:ooo'       : "http://openoffice.org/2004/office",
    'xmlns:ooow'      : "http://openoffice.org/2004/writer",
    'xmlns:oooc'      : "http://openoffice.org/2004/calc",
    'xmlns:dom'       : "http://www.w3.org/2001/xml-events",
    'xmlns:xforms'    : "http://www.w3.org/2002/xforms",
    'xmlns:xsd'       : "http://www.w3.org/2001/XMLSchema",
    'xmlns:xsi'       : "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:rpt'       : "http://openoffice.org/2005/report",
    'xmlns:of'        : "urn:oasis:names:tc:opendocument:xmlns:of:1.2",
    'xmlns:xhtml'     : "http://www.w3.org/1999/xhtml",
    'xmlns:grddl'     : "http://www.w3.org/2003/g/data-view#",
    'xmlns:officeooo' : "http://openoffice.org/2009/office",
    'xmlns:tableooo'  : "http://openoffice.org/2009/table",
    'xmlns:calcext'   : "urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0",
    'xmlns:field'     : "urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0",
    'xmlns:formx'     : "urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0",
    'xmlns:css3t'     : "http://www.w3.org/TR/css3-text/" ,
    'office:version'  : "1.2"
}

attrs_font_face = [
        ["Courier 10 Pitch", "&apos;Courier 10 Pitch&apos;", "fixed"],
        ["微软雅黑", "微软雅黑", "variable"]
        ]


doc = Document()

# 创建根元素
document_content = doc.createElement('office:document-content') #创建根元素
for key, value in attrs_document_content.items():
    document_content.setAttribute(key, value)
doc.appendChild(document_content)

# office:scripts 
scripts = doc.createElement('office:scripts')
document_content.appendChild(scripts)

# office:font-face-decls
font_face_decls = doc.createElement('office:font-face-decls')
for i in attrs_font_face:
    font_face = doc.createElement('style:font-face')
    font_face.setAttribute('style:name', i[0])
    font_face.setAttribute('style:font-family', i[1])
    font_face.setAttribute('style:font-pitch', i[2])
    font_face_decls.appendChild(font_face)
document_content.appendChild(font_face_decls)

"""

<style:style style:name="P1" style:family="paragraph" style:parent-style-name="Standard">
    <style:text-properties officeooo:paragraph-rsid="00173d7a"/>
</style:style>
<style:style style:name="P2" style:family="paragraph" style:parent-style-name="Table_20_Contents">
    <style:text-properties officeooo:paragraph-rsid="00173d7a"/>
</style:style>
<style:style style:name="P3" style:family="paragraph" style:parent-style-name="Table_20_Contents">
    <style:text-properties style:font-name="微软雅黑" officeooo:paragraph-rsid="00173d7a" style:font-name-asian="微软雅黑"/>
</style:style>
<style:style style:name="T1" style:family="text">
    <style:text-properties officeooo:rsid="00173d7a"/>
</style:style>
<style:style style:name="T2" style:family="text">
    <style:text-properties style:font-name="Courier 10 Pitch" officeooo:rsid="00173d7a"/>
</style:style>


"""
# office:automatic-styles
automatic_styles = doc.createElement('office:automatic-styles')
document_content.appendChild(automatic_styles)

# office:body
body = doc.createElement('office:body')
document_content.appendChild(body)

########### 将DOM对象doc写入文件
f = open('test2.xml','w')
#f.write(doc.toxml())
f.write(doc.toprettyxml(indent = '  '))
f.close()
