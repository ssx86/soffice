#!/usr/bin/python
#coding=utf-8
# xml文件读写的实验
#
#

#encoding:utf-8
'''
根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML。
'''
from xml.dom.minidom import Document

doc = Document()  #创建DOM文档对象

bookstore = doc.createElement('bookstore') #创建根元素
bookstore.setAttribute('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")#设置命名空间
bookstore.setAttribute('xsi:noNamespaceSchemaLocation','bookstore.xsd')#引用本地XML Schema
doc.appendChild(bookstore)
############book:Python处理XML之Minidom################
book = doc.createElement('book')
book.setAttribute('genre','XML')
bookstore.appendChild(book)

title = doc.createElement('title')
title_text = doc.createTextNode('Python处理XML之Minidom') #元素内容写入
title.appendChild(title_text)
book.appendChild(title)

author = doc.createElement('author')
book.appendChild(author)
author_first_name = doc.createElement('first-name')
author_last_name  = doc.createElement('last-name')
author_first_name_text = doc.createTextNode('张')
author_last_name_text  = doc.createTextNode('三')
author.appendChild(author_first_name)
author.appendChild(author_last_name)
author_first_name.appendChild(author_first_name_text)
author_last_name.appendChild(author_last_name_text)
book.appendChild(author)

price = doc.createElement('price')
price_text = doc.createTextNode('28')
price.appendChild(price_text)
book.appendChild(price)
############book1:Python写网站之Django####################
book1 = doc.createElement('book')
book1.setAttribute('genre','Web')
bookstore.appendChild(book1)

title1 = doc.createElement('title')
title_text1 = doc.createTextNode('Python写网站之Django')
title1.appendChild(title_text1)
book1.appendChild(title1)

author1 = doc.createElement('author')
book.appendChild(author1)
author_first_name1 = doc.createElement('first-name')
author_last_name1  = doc.createElement('last-name')
author_first_name_text1 = doc.createTextNode('李')
author_last_name_text1  = doc.createTextNode('四')
author1.appendChild(author_first_name1)
author1.appendChild(author_last_name1)
author_first_name1.appendChild(author_first_name_text1)
author_last_name1.appendChild(author_last_name_text1)
book1.appendChild(author1)

price1 = doc.createElement('price')
price_text1 = doc.createTextNode('40')
price1.appendChild(price_text1)
book1.appendChild(price1)

########### 将DOM对象doc写入文件
f = open('bookstore.xml','w')
f.write(doc.toxml())
#f.write(doc.toprettyxml(indent = ' '))
f.close()
