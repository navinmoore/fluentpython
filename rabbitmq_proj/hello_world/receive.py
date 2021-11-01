# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-25 17:34:32
# LastEditTime: 2021-10-25 17:49:34
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/rabbitmq_proj/hello_world/receive.py
# 

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare("hello")

def callback(ch, method, properties, body):
    print("[x] Received %r" % body)


# 需要告诉RabbitMQ这个回调函数将会从名为hello的队列中接受消息
channel.basic_consume(callback, queue='hello', no_ack=True)

# 最后，我们运行一个用来等待消息数据并且在需要的时候运行回调函数的无限循环。
channel.start_consuming()

print('end')