# -*- coding:utf-8 -*-
# @Filename: tasks
# @Date....: 2021-10-22 13:07
# @Author: yairs

from proj import app


@app.task
def add(x, y):
    print("task.add:", x, y)
    return x + y


@app.task
def mul(x, y):
    print("task.mul:", x, y)
    return x * y


@app.task
def xsum(numbers):
    print("task.xsum:", xsum)
    return sum(numbers)


