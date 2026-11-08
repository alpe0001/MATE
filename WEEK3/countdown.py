import time
while True:
    counter=input("Sayaç için bir sayı giriniz: ")
    if counter.isdigit():
        counter=int(counter)
        break
    else:
        print("Lütfen geçerli bir sayı giriniz.")
for i in range(counter,-1,-1):
    print(i)
    time.sleep(1)
print("Ateşle!")
