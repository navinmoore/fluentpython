# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-21 11:32:23
# LastEditTime: 2021-10-21 11:40:23
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/main1.py
# 

from threading import Thread

def func():
    for i in range(1000):
        print("func:{}".format(i))


if __name__ == '__main__':
    t = Thread(target=func, args=())
    t.start()
    for i in range(1000):
        print("main:{}".format(i))