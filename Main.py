
from TabloDuzenleyici import (
    tabloyu_getir,
    Ogrenci_ekle,
    Ogrenci_sil,
    not_degisim,
    ad_degisim,
    analiz
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
[6] Analiz
[7] Çıkış
""")


while True:

    try:
        secim = int(
            input("\nSeçiminiz: ")
        )

    except ValueError:
        print("Lütfen sayı giriniz.")
        continue


    if secim == 1:

        print("\n--- TABLO ---")
        print(tabloyu_getir())


    elif secim == 2:

        Ogrenci_ekle()

        print("\nGüncel Tablo:")
        print(tabloyu_getir())


    elif secim == 3:

        Ogrenci_sil()

        print("\nGüncel Tablo:")
        print(tabloyu_getir())


    elif secim == 4:

        not_degisim()

        print("\nGüncel Tablo:")
        print(tabloyu_getir())


    elif secim == 5:

        ad_degisim()

        print("\nGüncel Tablo:")
        print(tabloyu_getir())


    elif secim == 6:

        analiz()


    elif secim == 7:

        print("\nProgram kapatılıyor...")
        break


    else:

        print("Geçersiz seçenek.")
