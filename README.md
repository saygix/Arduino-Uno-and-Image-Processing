# El İzleme ve LED Kontrol Projesi

Bu proje, Python ve Arduino kullanarak el izleme teknolojisinin entegrasyonunu sağlamaktadır. Python tarafında Mediapipe kütüphanesi kullanılarak el izleme sonuçları elde edilir ve belirlenen el pozisyonlarına bağlı olarak Arduino'ya komutlar gönderilir. Arduino tarafında yazılan kod, bu komutları alarak kırmızı, yeşil ve sarı LED'leri kontrol eder.
<img src="https://github.com/saygix/Arduino-Uno-and-Image-Processing/assets/139467552/10d19e25-ae10-4ba9-bcbd-101c3fe5019c" alt="Resim Açıklaması" width="200" height="200">

## Kurulum

1. Arduino IDE'yi [buradan](https://www.arduino.cc/en/software) indirip yükleyin.
2. Python için gerekli kütüphaneleri yüklemek için terminal veya komut istemcisine şu komutu yazın: `pip install mediapipe pyserial`

## Kullanım

1. Arduino kodunu Arduino IDE'yi kullanarak Arduino kartınıza yükleyin.
2. Python kodunu çalıştırarak el izleme ve LED kontrolünü başlatın: `python el_izleme_led_kontrol.py`

## Proje Detayları

- Python ve Mediapipe ile el izleme teknolojisinin kullanımı
![alt El Hareketleri Algılandığında Alınan Görüntü ](![image](https://github.com/saygix/Arduino-Uno-and-Image-Processing/assets/139467552/9f659dc4-498b-4ad8-a560-30b61dbe1427)
)
- Arduino ile seri iletişim protokolü kullanılarak LED kontrolü
- Görüntü işleme ve fiziksel hesaplama arasındaki etkileşim


## Proje Sonuçları

Elde edilen sonuçlar, el izleme teknolojisinin interaktif uygulamalarda başarıyla kullanılabilirliğini ve Python ile Arduino'nun entegrasyonunun projelerde güçlü bir araç olduğunu göstermektedir.

## Katkıda Bulunma

Eğer projeye katkıda bulunmak istiyorsanız, lütfen bir çekme isteği oluşturun. Ayrıca, herhangi bir sorun veya öneriniz varsa GitHub sorun takibini kullanabilirsiniz.

