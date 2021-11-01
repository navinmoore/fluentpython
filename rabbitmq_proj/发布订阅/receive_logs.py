# -*-coding:utf-8-*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# exchange
channel.exchange_declare(exchange = 'logs', exchange_type = "fanout")

# queue
result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

# bind
channel.queue_bind(queue=queue_name, exchange='logs')


def callback(channel, method, properties, body):
    print(body, "###")

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()