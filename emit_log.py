import pika
import sys

connnection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connnection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ''.join(sys.argv[1:]) or "Hello World"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print("[x] Sent %r" % message)

connnection.close()