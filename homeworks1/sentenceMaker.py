while True:
    name = input("İsminiz: ")
    if name.isnumeric():
        print("Lütfen isminizi girin.")
    else:
        break
while True:
    surname = input("Soyisminiz: ")
    if surname.isnumeric():
        print("Lütfen soyisminizi girin.")
    else:
        break
city = input("Yaşadığınız şehir: ")

print(f"Veritabanı yeni kullanıcı girişi\nİsim: {name}\nSoyisim: {surname}\n İkametgah: {city}")