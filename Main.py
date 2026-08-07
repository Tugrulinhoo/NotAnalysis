from TabloDuzenleyici import (
    tabloyu_getir,
    Ogrenci_ekle,
    Ogrenci_sil,
    not_degisim,
    ad_degisim
)


print("""
========================================
          NOT ANALİZ PROGRAMI
========================================

[1] Tabloyu Göster
[2] Öğrenci Ekle
[3] Öğrenci Sil
[4] Not Değiştir
[5] İsim Değiştir
[6] Çıkış
""")


while True:

    try:
        secim = int(input("Seçiminiz: "))

    except ValueError:
        print("Lütfen sayı giriniz.")
        continue

    if secim == 1:
        print(tabloyu_getir())

    elif secim == 2:
        Ogrenci_ekle()
        print(tabloyu_getir())

    elif secim == 3:
        Ogrenci_sil()

    elif secim == 4:
        not_degisim()

    elif secim == 5:
        ad_degisim()

    elif secim == 6:
        print("Program kapatılıyor...")
        break

    else:
        print("Geçersiz seçenek.")
