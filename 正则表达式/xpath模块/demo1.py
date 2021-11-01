# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-20 17:37:50
# LastEditTime: 2021-10-21 10:14:54
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/正则表达式/xpath模块/demo1.py
# 
import re
from lxml import etree

html = etree.parse("example.html", etree.HTMLParser())

obj = re.compile('^\S(.*)')
print(dir(obj))
div_lis = html.xpath('//div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span')
# print(div_lis)
for i in div_lis:
    # print(i.text)
    a = obj.finditer(i.text)
    for i in a:
        print(i.group())