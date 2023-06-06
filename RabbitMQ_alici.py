import pika

# RabbitMQ sunucusuna bağlanma
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Mesajı almak için kuyruk tanımlama
channel.queue_declare(queue='MESAJKUYRUK')

# Mesaj işleme fonksiyonu
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# Mesaj işleme fonksiyonunu tanımlama

channel.basic_consume('MESAJKUYRUK',callback, True)

# Mesajları sürekli olarak dinleme
channel.start_consuming()

