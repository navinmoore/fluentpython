# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-20 15:28:03
# LastEditTime: 2021-10-20 16:18:20
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/正则表达式/re模块/demo1.py
# 

import re

s = """
    <ul class="list">
        <li class="top">
            <p class="overflowText" style="width: 100%;">PR</p>
        </li>
        <li class="middle">
            <div class="name" title="洪泰智造PPT模版.pptx" style="width: 100%;">
                <div class="img"><img src="/static/image/ppt.7b34e093.png" alt=""></div>
                <p class="overflowText">洪泰智造PPT模版.pptx</p>
            </div>
        </li>

        <li class="middle">
            <div class="name" title="洪泰智造议程类模版.docx" style="width: 100%;">
                <div class="img"><img src="/static/image/word.7db1ad91.png" alt=""></div>
                <p class="overflowText">洪泰智造议程类模版.docx</p>
            </div>
        </li>
        <li class="middle"><div class="name" title="洪泰智造介绍2021.v1.pdf" style="width: 100%;"><div class="img"><img src="/static/image/pdf.162b1d65.png" alt=""></div><p class="overflowText">洪泰智造介绍2021.v1.pdf</p></div></li><li class="middle"><div class="name" title="洪泰智造WORD模板.docx" style="width: 100%;"><div class="img"><img src="/static/image/word.7db1ad91.png" alt=""></div><p class="overflowText">洪泰智造WORD模板.docx</p></div></li></ul>
"""

obj = re.compile('<p class=.*?>(?P<h>.*?)</p>', re.S)

c = obj.finditer(s)
# c = obj.findall(s)
# print(c)

for i in c:
    print(i.group())
    print(i.group("h"))