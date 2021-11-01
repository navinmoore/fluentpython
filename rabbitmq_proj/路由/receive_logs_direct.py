# coding:utf-8

import pika
import sys

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="direct_logs", exchange_type='direct')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

severities = sys.argv[1:]

if not severities:
    print("Usage: %s [info] [warning] [error]" % (sys.argv[0],), file=sys.stderr)
    sys.exit(1)


for severity in severities:
    channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=severity)


print('[*] Warning for logs. To exit press CTRL+C')

def callback(channel, method, properties, body):
    print("[x] %r: %r" % (method.routing_key, body,))


channel.basic_consume(callback, result.method.queue, no_ack=True)

channel.start_consuming()

