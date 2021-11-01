# -*- coding:utf-8 -*-
# @Filename: __init__.py
# @Date....: 2021-10-22 13:05
# @Author: yairs
# celery -A proj worker -l INFO

from celery import Celery


app = Celery('proj')

app.config_from_object("proj.celeryconfig")