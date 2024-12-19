import pika
import json

# RabbitMQ bağlantısı
def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # Kuyruğu oluştur (bu adım zaten producer tarafından yapılmış olsa da güvenlik için burada da ekleniyor)
    channel.queue_declare(queue='orders')
    return channel

# Siparişi işleme
def process_order(ch, method, properties, body):
    order = json.loads(body)
    print(f" [x] Processing order: {order}")
    # Sipariş işleme işlemleri burada yapılır, örneğin veritabanına kaydetme, ödeme işlemi vs.
    print(f" Order processed for customer: {order['customer_name']}")

# Kuyruğu dinleme
def consume_orders():
    channel = connect_to_rabbitmq()
    channel.basic_consume(queue='orders', on_message_callback=process_order, auto_ack=True)

    print(' [*] Waiting for orders. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_orders()
