# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-26 11:36:46
# LastEditTime: 2021-10-26 14:40:13
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/rabbitmq_proj/队列/new_tasks.py
# 

import sys, pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = " ".join(sys.argv[1:]) or "Hello World!"

# result 为queue
result = channel.queue_declare("logs", durable=True)
# result.method.queue

# 每次给work给
channel.basic_qos(prefetch_count=1)



# channel.basic_publish(exchange="", routing_key="hello", body=message)
# 发送时，
channel.basic_publish(
    exchange='logs', 
    routing_key='', 
    body=message, 
    properties=pika.BasicProperties(delivery_mode=2,)
    )

print('[x] Send %r' % (message,))

connection.close()