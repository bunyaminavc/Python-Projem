"""
Kitap Takip Uygulaması
----------------------
Amaç: Okunan/okunacak kitapları ekleyen, listeleyen, durumunu
(okundu/okunmadı) güncelleyen ve silen basit bir konsol uygulaması.
Kitaplar 'kitaplar.json' dosyasında saklanır; program kapanıp açılınca
kayıtlar korunur.

Nasıl çalıştırılır:
- python3 kitap.py

İşlevler:
1. Kitapları Listele
2. Yeni Kitap Ekle (boş başlık/yazar kabul etmez)
3. Okundu/Okunmadı İşaretle
4. Kitap Sil
5. Çıkış (kayıtları dosyaya yazar)
"""

import json

DOSYA_ADI = "kitaplar.json"


def kitaplari_yukle():
    """Kayıtlı kitapları JSON dosyasından okur.

    Dosya yoksa veya bozuksa boş bir listeyle başlanır, program çökmez.
    """
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            kitaplar = json.load(dosya)
        print("Kitaplar başarıyla yüklendi.")
        return kitaplar
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı. Yeni bir liste oluşturuldu.")
        return []
    except json.JSONDecodeError:
        print("Kayıt dosyası okunamadı, yeni bir liste oluşturuldu.")
        return []


def kitaplari_kaydet(kitaplar):
    """Kitap listesini JSON dosyasına yazar."""
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            json.dump(kitaplar, dosya, ensure_ascii=False, indent=2)
        print("Kitaplar başarıyla kaydedildi.")
    except OSError:
        print("Kitaplar kaydedilirken bir hata oluştu.")


def kitaplari_listele(kitaplar):
    """Kitapları numaralandırarak başlık, yazar ve durumuyla listeler."""
    if not kitaplar:
        print("Henüz kayıtlı kitap yok.")
        return

    print("--- KİTAP LİSTESİ ---")
    for index, kitap in enumerate(kitaplar, start=1):
        print(f"{index}. {kitap['baslik']} — {kitap['yazar']} [{kitap['durum']}]")
    print("---------------------")


def kitap_ekle(kitaplar):
    """Kullanıcıdan başlık ve yazar alıp listeye yeni kitap ekler."""
    baslik = input("Kitap başlığı: ").strip()
    if not baslik:
        print("Başlık boş olamaz!")
        return

    yazar = input("Yazar: ").strip()
    if not yazar:
        print("Yazar boş olamaz!")
        return

    yeni_kitap = {"baslik": baslik, "yazar": yazar, "durum": "okunmadı"}
    kitaplar.append(yeni_kitap)
    print(f"'{baslik}' eklendi.")
    kitaplari_kaydet(kitaplar)


def durum_degistir(kitaplar):
    """Kitap numarasına göre okundu/okunmadı durumunu değiştirir."""
    if not kitaplar:
        print("Henüz kayıtlı kitap yok.")
        return

    kitaplari_listele(kitaplar)
    girdi = input("Durumunu değiştirmek istediğiniz kitabın numarası: ").strip()

    try:
        numara = int(girdi)
    except ValueError:
        print("Lütfen bir sayı girin!")
        return

    if numara < 1 or numara > len(kitaplar):
        print("Geçersiz kitap numarası!")
        return

    kitap = kitaplar[numara - 1]
    if kitap["durum"] == "okunmadı":
        kitap["durum"] = "okundu"
    else:
        kitap["durum"] = "okunmadı"

    print(f"'{kitap['baslik']}' artık [{kitap['durum']}] olarak işaretlendi.")
    kitaplari_kaydet(kitaplar)


def kitap_sil(kitaplar):
    """Kitap numarasına göre listeden kitap siler."""
    if not kitaplar:
        print("Henüz kayıtlı kitap yok.")
        return

    kitaplari_listele(kitaplar)
    girdi = input("Silmek istediğiniz kitabın numarası: ").strip()

    try:
        numara = int(girdi)
    except ValueError:
        print("Lütfen bir sayı girin!")
        return

    if numara < 1 or numara > len(kitaplar):
        print("Geçersiz kitap numarası!")
        return

    silinen_kitap = kitaplar.pop(numara - 1)
    print(f"'{silinen_kitap['baslik']}' silindi.")
    kitaplari_kaydet(kitaplar)


def menu_goster():
    """Ana menüyü ekrana yazdırır."""
    print("\n--- KİTAP TAKİP UYGULAMASI ---")
    print("1. Kitapları Listele")
    print("2. Yeni Kitap Ekle")
    print("3. Okundu/Okunmadı İşaretle")
    print("4. Kitap Sil")
    print("5. Çıkış")


def ana_program():
    """Programın ana döngüsü: menüyü gösterir, kullanıcı seçimine göre işlem yapar."""
    print("Kitap Takip Uygulamasına Hoş Geldiniz!")
    kitaplar = kitaplari_yukle()

    while True:
        menu_goster()
        secim = input("Seçiminiz (1-5): ").strip()

        if secim == "1":
            kitaplari_listele(kitaplar)
        elif secim == "2":
            kitap_ekle(kitaplar)
        elif secim == "3":
            durum_degistir(kitaplar)
        elif secim == "4":
            kitap_sil(kitaplar)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-5 arası bir değer girin.")


if __name__ == "__main__":
    ana_program()
