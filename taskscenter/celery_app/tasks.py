# coding:utf-8
from  celery_app import app


@app.task
def add(x, y):
    print("task.add:", x, y)
    return x + y


@app.task
def taskA(x, y):
    print("task.taskA:", x, y)
    return x + y

@app.task
def taskB(x, y):
    print("task.taskB:", x, y)
    return x + y


@app.task
def schedule(x, y):
    print("task.schedule:", x, y)
    return x + y

@app.task
def cron(x, y):
    print("task.cron:", x, y)
    return x + y


