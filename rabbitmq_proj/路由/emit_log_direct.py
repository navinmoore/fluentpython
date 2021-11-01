# coding:utf-8

import pika
import sys

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# 交换机
exchange = channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

message = " ".join(sys.argv[2:]) or "Hello World"

# basic_publish(self, exchange, routing_key, body, properties=None, mandatory=False, immediate=False)
channel.basic_publish(exchange="direct_logs", routing_key=severity, body=message)

print("[x] Sent %r:%r" % (severity, message))

connection.close()
