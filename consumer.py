import pika #menggunakan library pika
import sys  #menggunakan library system
import os   #menggunakan libray Operating System

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))   #parameter menggunakan localhost
    channel = connection.channel()  #memulai sebuah channel

    channel.queue_declare(queue='EAI') #mendeclare sebuah queue

    def callback(ch, method, properties, body): #code ini akan mencetak sebuah pesan yang dikirimkan dari producer
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='EAI', on_message_callback=callback, auto_ack=True) #code ini akan menerima pesan yang dikirimkan dari producer dengan queue EAI

    print('Sedang menunggu pesan, klik CTRL + C untuk keluar!')
    channel.start_consuming()   #memulai untuk menerima pesan dari queue EAI yang dikirimkan oleh producer

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)