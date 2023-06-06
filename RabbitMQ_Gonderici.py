import pika

# RabbitMQ sunucusuna bağlanma
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Mesajı göndermek için kuyruk tanımlama
channel.queue_declare(queue='MESAJKUYRUK')

# Mesajı gönderme
channel.basic_publish(exchange='', routing_key='MESAJKUYRUK', body='Merhaba RabbitMQ!')

# Bağlantıyı kapatma
connection.close()