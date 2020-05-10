
koltuklar = [[-1 for x in range(20)] for y in range(20)]


def ana_menu() :
    print("***************")
    print("** ANA MENÜ  **")
    print("***************")
    print("1. Rezervasyon")
    print("2. Salonu Yazıdr")
    print("3. Yeni Etkinlik")
    print("0. Çıkış")
    print("****************")
    secim = int(input("seçiminiz"))
    return secim

def dolu_mu(kategori,adet):
    if(kategori == 1):
        toplam = 0
        for i in range(0, 10):
            for j in range(5, 15):
                if(koltuklar[i][j] == 1):
                    toplam = toplam + 1

        if(100-toplam < adet):
            print("Bu kategoride yer kalmamıştır")
            return True

    if(kategori == 2):
        toplam = 0
        for i in range(0, 10):
            for j in range(0, 5):
                if(koltuklar[i][j] == 1):
                    toplam = toplam + 1

        for i in range(0, 10):
            for j in range(15, 20):
                if(koltuklar[i][j] == 1):
                    toplam = toplam + 1
        if(100-toplam < adet):
            print("Bu kategoride yer kalmamıştır")
            return True

    if(kategori == 3):
        toplam = 0
        for i in range(10, 20):
            for j in range(5, 15):
                if(koltuklar[i][j] == 1):
                    toplam = toplam + 1

        if(100-toplam < adet):
            print("Bu kategoride yer kalmamıştır")
            return True

    if(kategori == 4):
        toplam = 0
        for i in range(10, 20):
            for j in range(0, 5):
                if (koltuklar[i][j] == 1):
                    toplam = toplam + 1

        for i in range(10, 20):
            for j in range(15, 20):
                if (koltuklar[i][j] == 1):
                    toplam = toplam + 1
        if (100 - toplam < adet):
            print("Bu kategoride yer kalmamıştır")
            return True


while True:


    islem = ana_menu()

    if islem == 0:
        print("Program Kapatılıyor...")
        break
    elif islem == 1 :                                                       #Rezervasyon

        verilen_koltuklar = []
        while True:
            while True:
                try:
                    kategori = int(input("Kategori (1-4)"))
                    if(kategori < 0 or kategori >4):
                        raise ValueError
                    break
                except ValueError:
                    print("Aralikta Deger Giriniz")

            while True:
                try:
                    adet = int(input("Bilet Adedi (1-10)"))
                    if(adet < 0 or adet >10):
                        raise ValueError
                    break
                except ValueError:
                    print("Aralikta Deger Giriniz")

            if(not dolu_mu(kategori,adet)):
                break



        print("Rezerve Edilen Koltuklar (Sıra-Koltuk)",end=" ")


        if(kategori == 1):
            sayac = 0
            verilen_koltuklar.clear()
            for i in range(0,10):
                for j in range(5,15):
                    if(sayac==adet):
                        break
                    elif(koltuklar[i][j]==1):
                        continue
                    else:
                        koltuklar[i][j] = 1
                        sayac+=1
                        verilen_koltuklar.append(i+1)
                        verilen_koltuklar.append(j+1)
            for i in range(0, len(verilen_koltuklar) - 1, 2):
                print("{} - {},".format(verilen_koltuklar[i], verilen_koltuklar[i + 1]), end=" ")
            print("\n")

        elif(kategori == 2):
            verilen_koltuklar.clear()
            sayac = 0
            dizi = [4,3,2,1,0,15,16,17,18,19]
            for i in range(0, 10):
                for j in dizi:
                    if(koltuklar[i][19]==1):
                        continue
                    if (sayac == adet):
                        break
                    elif (koltuklar[i][j] == 1):
                        continue

                    else:
                        koltuklar[i][j] = 1
                        sayac += 1
                        verilen_koltuklar.append(i+1)
                        verilen_koltuklar.append(j+1)
            for i in range(0,len(verilen_koltuklar)-1,2):
                print("{} - {},".format(verilen_koltuklar[i],verilen_koltuklar[i+1]),end=" ")
            print("\n")


        elif(kategori == 3):
            verilen_koltuklar.clear()
            sayac = 0
            for i in range(10, 20):
                for j in range(5, 15):
                    if (sayac == adet):
                        break
                    elif (koltuklar[i][j] == 1):
                        continue
                    else:
                        koltuklar[i][j] = 1
                        sayac += 1
                        verilen_koltuklar.append(i+1)
                        verilen_koltuklar.append(j+1)
            for i in range(0, len(verilen_koltuklar) - 1, 2):
                print("{} - {},".format(verilen_koltuklar[i], verilen_koltuklar[i + 1]), end=" ")
            print("\n")

        elif(kategori == 4):
            verilen_koltuklar.clear()
            sayac = 0
            dizi = [4, 3, 2, 1, 0, 15, 16, 17, 18, 19]
            for i in range(10, 20):
                for j in dizi:
                    if (koltuklar[i][19] == 1):
                        continue
                    if (sayac == adet):
                        break
                    elif (koltuklar[i][j] == 1):
                        continue
                    else:
                        koltuklar[i][j] = 1
                        sayac += 1
                        verilen_koltuklar.append(i+1)
                        verilen_koltuklar.append(j+1)
            for i in range(0, len(verilen_koltuklar) - 1, 2):
                print("{} - {},".format(verilen_koltuklar[i], verilen_koltuklar[i + 1]), end=" ")
            print("\n")

    elif islem == 2:
        for i in range(20):
            for j in range(20):
                if(koltuklar[i][j]==1):
                    print("x", end="")
                else:
                    print("-", end="")
            print("\n",end="")
    else :                                                  #Sahneyi sıfırlama
        for i in range(20):
            for j in range(20):
                koltuklar[i][j]=0












