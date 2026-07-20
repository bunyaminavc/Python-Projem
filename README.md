# Kitap Takip Uygulaması

Basit, konsol tabanlı bir kişisel kütüphane / kitap takip uygulaması. Python ile yazılmıştır, harici kütüphane gerektirmez.

## Özellikler

- Kitap ekleme (başlık, yazar; varsayılan durum "okunmadı")
- Kitapları numaralandırılmış şekilde listeleme
- Kitabın durumunu okundu/okunmadı olarak değiştirme
- Kitap silme
- Kayıtlar `kitaplar.json` dosyasında saklanır; program kapatılıp açıldığında veriler kaybolmaz

## Gereksinimler

- Python 3

Harici/üçüncü parti kütüphane kullanılmaz (sadece standart kütüphaneden `json`).

## Çalıştırma

```bash
python3 kitap.py
```

## Kullanım

Program açıldığında bir menü gösterilir:

```
--- KİTAP TAKİP UYGULAMASI ---
1. Kitapları Listele
2. Yeni Kitap Ekle
3. Okundu/Okunmadı İşaretle
4. Kitap Sil
5. Çıkış
Seçiminiz (1-5):
```

1-5 arası bir numara girerek ilgili işlemi seçersiniz. Geçersiz bir seçim yapıldığında (örn. sayı dışı bir menü değeri veya kitap numarası yerine harf) program çökmez, kontrollü bir hata mesajı gösterir.

## Veri Modeli

Her kitap şu şekilde bir sözlük (dict) olarak tutulur:

```json
{"baslik": "1984", "yazar": "George Orwell", "durum": "okunmadı"}
```

Tüm kitaplar bu sözlüklerden oluşan bir liste halinde `kitaplar.json` dosyasına yazılır (UTF-8, Türkçe karakter desteği).

## Dosya Yapısı

- `kitap.py` — uygulamanın tamamı (tek dosya)
- `kitaplar.json` — program ilk çalıştırıldığında otomatik oluşturulur, kayıtları tutar
