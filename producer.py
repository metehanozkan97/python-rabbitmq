import pika
import json
import time

# RabbitMQ bağlantısı
def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # Kuyruğu oluştur
    channel.queue_declare(queue='orders')
    return channel

# Sipariş verisi oluştur
def create_order():
    order = {
        "customer_name": "Metehan Özkan",
        "order_id": 12345,
        "items": ["Laptop", "Mouse", "Keyboard"],
        "total_amount": 1200.50
    }
    return order

# Siparişi kuyruğa gönder
def send_order_to_queue(order):
    channel = connect_to_rabbitmq()
    # Siparişi JSON formatında kuyruğa gönder
    channel.basic_publish(
        exchange='',
        routing_key='orders',
        body=json.dumps(order)
    )
    print(f" [x] Sent order: {order}")

if __name__ == "__main__":
    order = create_order()
    send_order_to_queue(order)
    time.sleep(1)  # Üretici işlemi bitmeden önce biraz bekleyelim
