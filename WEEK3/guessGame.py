import random
number=random.randint(1,100)
guess=int(input("1 ile 100 arasında bir sayı tahmin edin(1 ve 100 dahil): "))
counter=1
while guess!=number:
    counter+=1
    if guess<number:
        print("Daha büyük bir sayı tahmin edin.")
    else:
        print("Daha küçük bir sayı tahmin edin.")
    guess=int(input("1 ile 100 arasında bir sayı tahmin edin(1 ve 100 dahil): "))
else:
    print(f"Tebrikler! Doğru tahmin ettiniz. Sayı: {number}\n{counter} tahminde doğru sayıyı buldunuz.")
