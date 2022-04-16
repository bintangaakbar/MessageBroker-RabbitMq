import pika  #menggunakan library pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='EAI')  #mendeklarasikan queue di rabbitmq menggunakan nama EAI

body = input("Masukkan Pesan anda: ")   #inputan user untuk mengirimkan pesan
channel.basic_publish(exchange='', routing_key='EAI', body=body)    #mengirimkan pesan menggunakan queue EAI dengan isi pesan dari inputan user
print(" [x] Mengirimkan", body) #bukti kalau code sudah berjalan
connection.close() #koneksi code dengan rabbitmq langsung di tutup setelah pesan terkirim