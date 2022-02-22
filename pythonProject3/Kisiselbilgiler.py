isim = input("Adınızı giriniz:")
soyisim = input("Soyisminizi giriniz:")
while True:
    TcKimlikNo = input("12 Haneli Tc Kimlik numaranızı giriniz:")
    toplam_uzunluk2 = len(TcKimlikNo)
    heskodu = input("10 haneli Hes Kodunuzu giriniz:")
    toplam_uzunluk = len(heskodu)
    if (toplam_uzunluk2 == 12):
        break
    elif (toplam_uzunluk2 < 10):
        print("TC kimlik numaranızı yanlış girdiniz. Lütfen tekrar deneyiniz.")
        continue
    if (toplam_uzunluk == 10):
        break
    elif (toplam_uzunluk < 10):
        print("Hes Kodunu yanlış girdiniz. Lütfen tekrar deneyiniz.")
        continue