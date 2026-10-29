def indirim_hesapla():
    while True:
        priceinput=input("Ürünün indirimsiz fiyatını giriniz: ")
        if "½" in priceinput:
            print("Lütfen geçerli bir sayı giriniz. ")
            continue
        if priceinput.isnumeric():
            priceinput = float(priceinput)
            break
        else:
            print("Lütfen geçerli bir sayı giriniz.")
    while True:
        offinput=input("Ürüne uygulanacak indirimi giriniz: %")
        if "½" in offinput:
            print("Lütfen geçerli bir sayı giriniz.")
            continue
        if offinput.isnumeric():
            offinput = float(offinput)
            if offinput>=100:
                print("Bu iş batmayı haketmiyor.")
            else:
                break
        print("Lütfen geçerli bir sayı giriniz.")
    lastprice = (priceinput)*((100-offinput)/100)
    return f"Ürününüzün ilk fiyatı: {priceinput}\nUygulanacak indirim oranı: %{offinput}\nÜrününüzün etiket fiyatı: {lastprice}"
while True:
    output = indirim_hesapla()
    print(output)
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