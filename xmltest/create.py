#!/usr/bin/python
#coding=utf-8
# xml�ļ���д��ʵ��
#
#

#encoding:utf-8
'''
����һ��������XML Schema��ʹ��DOM������ʽ�ӿհ��ļ�����һ��XML��
'''
from xml.dom.minidom import Document

doc = Document()  #����DOM�ĵ�����

bookstore = doc.createElement('bookstore') #������Ԫ��
bookstore.setAttribute('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")#���������ռ�
bookstore.setAttribute('xsi:noNamespaceSchemaLocation','bookstore.xsd')#���ñ���XML Schema
doc.appendChild(bookstore)
############book:Python����XML֮Minidom################
book = doc.createElement('book')
book.setAttribute('genre','XML')
bookstore.appendChild(book)

title = doc.createElement('title')
title_text = doc.createTextNode('Python����XML֮Minidom') #Ԫ������д��
title.appendChild(title_text)
book.appendChild(title)

author = doc.createElement('author')
book.appendChild(author)
author_first_name = doc.createElement('first-name')
author_last_name  = doc.createElement('last-name')
author_first_name_text = doc.createTextNode('��')
author_last_name_text  = doc.createTextNode('��')
author.appendChild(author_first_name)
author.appendChild(author_last_name)
author_first_name.appendChild(author_first_name_text)
author_last_name.appendChild(author_last_name_text)
book.appendChild(author)

price = doc.createElement('price')
price_text = doc.createTextNode('28')
price.appendChild(price_text)
book.appendChild(price)
############book1:Pythonд��վ֮Django####################
book1 = doc.createElement('book')
book1.setAttribute('genre','Web')
bookstore.appendChild(book1)

title1 = doc.createElement('title')
title_text1 = doc.createTextNode('Pythonд��վ֮Django')
title1.appendChild(title_text1)
book1.appendChild(title1)

author1 = doc.createElement('author')
book.appendChild(author1)
author_first_name1 = doc.createElement('first-name')
author_last_name1  = doc.createElement('last-name')
author_first_name_text1 = doc.createTextNode('��')
author_last_name_text1  = doc.createTextNode('��')
author1.appendChild(author_first_name1)
author1.appendChild(author_last_name1)
author_first_name1.appendChild(author_first_name_text1)
author_last_name1.appendChild(author_last_name_text1)
book1.appendChild(author1)

price1 = doc.createElement('price')
price_text1 = doc.createTextNode('40')
price1.appendChild(price_text1)
book1.appendChild(price1)

########### ��DOM����docд���ļ�
f = open('bookstore.xml','w')
f.write(doc.toxml())
#f.write(doc.toprettyxml(indent = ' '))
f.close()
