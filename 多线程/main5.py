# -*- coding:utf-8 -*-
# @Filename: main5
# @Date....: 2021-10-21 15:18
# @Author: yairs
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def func(name):
    for i in range(100):
        print("{}:{}".format(name, i))
    return name


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:
        fns = [pool.submit(func, name="name{}".format(name)) for name in range(10)]
        for f in as_completed(fns):
            print(f.result(), "here")


