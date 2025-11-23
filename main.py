print("--- Basit Hesap Makinesi ---")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("İşlem numarasını seç (1-4): ")

sayi1 = float(input("Birinci sayı: "))
sayi2 = float(input("İkinci sayı: "))

if secim == '1':
    sonuc = sayi1 + sayi2
    print("Sonuç:", sonuc)
elif secim == '2':
    sonuc = sayi1 - sayi2
    print("Sonuç:", sonuc)
elif secim == '3':
    sonuc = sayi1 * sayi2
    print("Sonuç:", sonuc)
elif secim == '4':
    if sayi2 == 0:
        print("Hata: Bir sayı 0'a bölünemez!")
    else:
        sonuc = sayi1 / sayi2
        print("Sonuç:", sonuc)
else:
    print("Yanlış bir seçim yaptın.")