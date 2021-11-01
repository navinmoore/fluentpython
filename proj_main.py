# -*- coding:utf-8 -*-
# @Filename: proj_main
# @Date....: 2021-10-22 13:10
# @Author: yairs
from proj.tasks import add

if __name__ == '__main__':
    results = []
    for i in range(100):
        result = add.delay(1, 2)
        results.append(result)
    for i in results:
        print(i.status)
