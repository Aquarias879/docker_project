import pika
import time
import database
import logging
import warnings
import json
import sys

connection = pika.BlockingConnection(
             pika.ConnectionParameters(host='192.168.0.45'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_qos(prefetch_count=1)


def callback(ch, method, properties, body):
    db_response = dbds.insert_db(body.decode())
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
