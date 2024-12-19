# RabbitMQ Order Processing System

Bu proje, RabbitMQ kullanarak basit bir sipariş işleme sistemini göstermektedir. Sistem, bir üretici (producer) ve bir tüketici (consumer) bileşeninden oluşmaktadır.

## Gereksinimler

- Python 3.x
- pika (RabbitMQ client)
- RabbitMQ Server

## Kurulum

1. RabbitMQ Server'ı yükleyin:   ```bash
   # Ubuntu/Debian için
   sudo apt-get install rabbitmq-server

   # macOS için
   brew install rabbitmq   ```

2. Gerekli Python paketlerini yükleyin:   ```bash
   pip install pika   ```

## Kullanım

1. RabbitMQ servisini başlatın:   ```bash
   # Ubuntu/Debian için
   sudo service rabbitmq-server start

   # macOS için
   brew services start rabbitmq   ```

2. Consumer'ı başlatın:   ```bash
   python consumer.py   ```

3. Yeni bir terminal açın ve Producer'ı çalıştırın:   ```bash
   python producer.py   ```

## Proje Yapısı

- `producer.py`: Örnek sipariş verisi oluşturup RabbitMQ kuyruğuna gönderen üretici script
- `consumer.py`: RabbitMQ kuyruğundan siparişleri alıp işleyen tüketici script

## Özellikler

- Asenkron mesaj iletimi
- JSON formatında veri transferi
- Otomatik kuyruk oluşturma
- Basit sipariş işleme mantığı

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje [MIT lisansı](LICENSE) altında lisanslanmıştır.