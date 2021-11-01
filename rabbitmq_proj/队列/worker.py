# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-26 12:52:37
# LastEditTime: 2021-10-26 13:53:30
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/rabbitmq_proj/队列/worker.py
# 

import pika, time

def callback(channel, method, properities, body):
    print('[x] Received %r' % (body,))
    time.sleep(str(body).count("."))
    print('[x] Done')
    channel.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

# channel.basic_consume(callback, "hello", no_ack=True)
channel.basic_consume(callback, 'hello')


channel.start_consuming()

