#Harf/Not karşılıkları
#81-100 AA
#71-80.99 BA
#61-70.99 BB
#56-60.99 CB
#49-55.99 CC
#40-48.99 DC
#25-39.99 GG
#10-24.99 FD
#00-9.99 FF
#not: herhangi bir standart belirtilmediği için karşılıkları rastgele aldım
#--------------------------------------
def not_hesaplama():
    #-------Sınav kredi oranları
    midtermRatio=0.4
    finalRatio=0.6
    #--------------------
    #-------Input alma
    while True:
        while True:
            midtermInput=input("Vize notunu giriniz: ")
            if midtermInput.isnumeric():
                if "½" in midtermInput:
                    print("Lütfen geçerli bir puan giriniz.")
                    continue
                midtermInput=float(midtermInput)
                if 0<=midtermInput<=100:
                    break
            print("Lütfen geçerli bir puan giriniz.")
        while True:
            finalInput=input("Final notunu giriniz: ")
            if finalInput.isnumeric():
                if "½" in finalInput:
                    print("Lütfen geçerli bir puan giriniz.")
                    continue
                finalInput=float(finalInput)
                if 0<=finalInput<=100:
                    break
            print("Lütfen geçerli bir puan giriniz.")
        break
    #-------Ortalama Hesaplama
    result=(midtermInput*midtermRatio)+(finalInput*finalRatio)
    #---------------------------------
    #---------Ortalama/Harf karşılıkları
    letternote = "FF"
    if result>=81:
        letternote = "AA"
    elif result>=71:
        letternote = "BA"
    elif result>=61:
        letternote = "BB"
    elif result>=56:
        letternote = "CB"
    elif result>=49:
        letternote = "CC"
    elif result>=40:
        letternote = "DC"
    elif result>=25:
        letternote= "GG"
    elif result>=10:
        letternote = "FD"
    else:
        letternote = "FF"
    #not:bu elifleri tek tek yazmaktan daha kolay bir yol varsa lütfen söyleyin
    #-------------------------
    #--------Geçme durumu
    if result>=40:
        ispass="Geçtiniz."
    else:
        ispass="Kaldınız."
    #------------------------
    print(f"Vize puanınız: {str(midtermInput)}\nFinal puanınız: {str(finalInput)}\nOrtalamanız: {str(result)}\nHarf notunuz: {letternote}\nGeçme Durumu: {ispass}")


while True:
    not_hesaplama()
    while True:
        cont = input('Çıkış için "Ç", devam etmek için "D" tuşlayın: ')
        cont2 = cont.upper()
        if cont2 == "Ç":
            break
        elif cont2 == "D":
            break
        else:
            print("Lütfen geçerli bir değer girin.")
            continue
    if cont2 == "Ç":
        break
    else:
        continue