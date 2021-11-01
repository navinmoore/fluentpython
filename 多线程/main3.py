# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-21 13:46:31
# LastEditTime: 2021-10-21 13:48:04
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/main3.py
# 

from multiprocessing.dummy import Pool as ThreadPool


def func(name):
    for i in range(10):
        print("thread:{},i={}".format(name, i))


if __name__ == '__main__':
    p = ThreadPool(2)

    p.apply_async(func, args=("t1",))
    p.apply_async(func, args=("t2",))
    p.apply_async(func, args=("t3",))
    p.apply_async(func, args=("t4",))

    p.close()
    p.join()
    print("end")