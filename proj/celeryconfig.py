# -*- coding:utf-8 -*-
# @Filename: celeryconfig
# @Date....: 2021-10-22 15:16
# @Author: yairs


broker_url = "pyamqp://guest@localhost//"
result_backend = "redis://localhost"
# include = ['proj.tasks']

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

imports = ("proj.tasks",)
