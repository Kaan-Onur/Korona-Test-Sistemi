while True:
    import Kisiselbilgiler
    print("Adınız:", Kisiselbilgiler.isim)
    print("Soyadınız:", Kisiselbilgiler.soyisim)
    print("Hes Kodunuz:", Kisiselbilgiler.heskodu)
    print("Tc Kimlik Numaranız:", Kisiselbilgiler.TcKimlikNo)
    soru=input("Bugün halsiz misiniz?(E/H)")
    if (soru=="E" or soru=="e"):
        print("")

    elif(soru=="H" or soru2=="h"):
        print("Sağlıklısınız. Maske, Mesafe ve temizliğe uyun.")
        break
    soru2= input("Ateşiniz Var mı?(E/H)")
    if(soru2=="E" or soru2=="e"):
        print("")
    elif(soru2=="H" or soru2=="h"):
        print("Evinizde dinlenin. Sosyal mesafeye uyun.")
        break
    soru3=input("Tat almada zorluk yaşıyor musunuz?(E/H)")
    if(soru3=="E" or soru3=="e"):
        print("Koronavirüs(Covid-19) testi yaptırmalısınız.")
        break
    elif(soru3=="H" or soru3=="h"):
        print("Covid-19 olma riskiniz var. En yakın sağlık kuruluşuna gidip test yaptırmalısınız.")
        continue