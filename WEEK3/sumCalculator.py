def Calculator(number):
    return number*(number+1)/2
while True:
    number=input("Lütfen geçerli bir tam sayı giriniz: ")
    if number.isdigit():
        number=int(number)
        break
    else:
        print("Lütfen geçerli bir sayı giriniz.")
print("1'den",str(number)+"'e kadar olan sayıların toplamı:",int(Calculator(number)))