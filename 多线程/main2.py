# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-21 11:40:32
# LastEditTime: 2021-10-21 13:41:11
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/main2.py
# 
from threading import Thread
import time


class MyThread(Thread):

    def run(self):
        for i in range(100):
            time.sleep(0.1)
            print('threading:{}'.format(i))


if __name__ == '__main__':
    t = MyThread()
    t.start()

    for i in range(100):
        time.sleep(0.1)
        print("main:{}".format(i))
