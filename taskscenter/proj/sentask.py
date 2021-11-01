# coding:utf-8


from demoapp.tasks import add

add.delay(1, 2)