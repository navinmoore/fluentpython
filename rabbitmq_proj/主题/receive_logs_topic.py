# coding:utf-8

import pika
import sys

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


binding_keys = sys.argv[1:]

if not binding_keys:
    print("Usage: %s [binding_keys]..." % (sys.argv[0],))
    sys.exit(1)


for key in binding_keys:
    channel.queue_bind(queue=queue_name, exchange="topic_logs", routing_key=key)

print('[x] Waiting for logs. To exit press CTRL+C')

def callback(channel, method, properties, body):
    print('[x] %r:%r' % (method.routing_key, body,))
    


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()