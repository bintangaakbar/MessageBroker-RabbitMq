#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='EAI')

body = input("Masukkan Pesan anda: ")
channel.basic_publish(exchange='', routing_key='EAI', body=body)
print(" [x] Mengirimkan", body)
connection.close()