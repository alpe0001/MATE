while True:
    try:
        number=float(input("Lütfen bir sayı giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        continue
print("Girdiğiniz sayı:",number)