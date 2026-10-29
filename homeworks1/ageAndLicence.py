currentYear = 2026
#licencexx->xx yaş sınırını temsil eder
licence16 = ["M1","A1","B1"]
licence18 = ["A2","B","BE","C1","F","G"]
licence20 = ["A"]
licence21 = ["C","CE","D1","D1E"]
licence24 = ["D","DE"]
while True:
    birthYear = input("Doğduğunuz yıl: ")
    if "½" in birthYear:
        print("Lütfen geçerli bir yıl girin.")
        continue
    elif birthYear.isnumeric() == 0:
        print("Lütfen geçerli bir yıl giriniz.")
        continue
    birthYear = int(birthYear)
    if birthYear > currentYear:
        print("Lütfen geçerli bir yıl girin.")
        continue
    age = currentYear - birthYear
    break
print(f"Yaşınız: {age}\nAlabileceğiniz ehliyetler:")
if age<16:
    print("Alabileceğiniz ehliyet yok.")
elif age<18:
    for i in licence16:
        print(i)
elif age<20:
    for i in licence16:
        print(i)
    for i in licence18:
        print(i)
elif age<21:
    for i in licence16:
        print(i)
    for i in licence18:
        print(i)
    print("A(En az 2 yıllık A2 deneyimi şartı aranır.)")
elif age<24:
    for i in licence16:
        print(i)
    for i in licence18:
        print(i)
    print("A(En az 2 yıllık A2 deneyimi şartı aranır.)")
    for i in licence21:
        print(i)
else:
    for i in licence16:
        print(i)
    for i in licence18:
        print(i)
    print("A(Deneyim şartı olmaksızın.)")
    for i in licence21:
        print(i)
    for i in licence24:
        print(i)