# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-20 16:22:11
# LastEditTime: 2021-10-21 09:16:46
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/正则表达式/re模块/demo2.py
# 
import requests, re

url = "http://movie.douban.com/top250"

headers = {
    # "Connection": "keep-alive",
     "Connection": "close",
    "Cache-Control": "max-age=0",
    
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
   
}
resp = requests.get(url, headers=headers)


# print(dir(resp))
resp_content = resp.content.decode('utf-8').replace(' ', '').replace('  ', '').replace("\r\n", "")
print(resp_content)
# resp.close()

str = '''<div class="info">.*?<span class="title">(?P<name>)</span>.*?</div><div class="bd"><p class="">.*?<br>(?P<year>\d+).*?
                        </p>

                        
                        <div class="star">
                                <span>(?P<people>\d+)人评价</span>
                        </div>

                    </div>
                </div>
                        '''

# str = str.strip(" ").strip("  ")
# obj = re.compile(str, re.S|re.X)


# iterobj = obj.findall(resp_content)
# print(iterobj)
# iterobj = obj.finditer(resp_content)
# print(dir(iterobj))
# for i in iterobj:
#     print(i.group("cn_name"), i.group("year"))
    
    