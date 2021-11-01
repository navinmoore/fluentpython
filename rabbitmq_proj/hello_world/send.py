# -*- coding:utf-8 -*-
# @Filename: send
# @Date....: 2021-10-22 17:18
# @Author: yairs

import pika

# 建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建名为hello的队列
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key="hello", body="Hello World!")


while True:
    pass