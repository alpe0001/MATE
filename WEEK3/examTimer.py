import datetime
while True:
    inputDateTime=input("Lütfen belirtilen formatta geçerli bir tarih ve saat giriniz (Gün-Ay-Yıl Saat:Dakika:Saniye): ")
    if len(inputDateTime)==19 and inputDateTime[2]=='-' and inputDateTime[5]=='-' and inputDateTime[10]==' ' and inputDateTime[13]==':' and inputDateTime[16]==':':
        try:
            dateTimeExam=datetime.datetime.strptime(inputDateTime, '%d-%m-%Y %H:%M:%S')
            if dateTimeExam<datetime.datetime.now():
                print("Lütfen ileri bir tarih ve saat giriniz.")
                continue
            break
        except ValueError:
            continue
dateTimeNow = datetime.datetime.now()
dateTimeNow = dateTimeNow.strftime('%d-%m-%Y %H:%M:%S')
remainingDateTime=dateTimeExam-datetime.datetime.strptime(dateTimeNow, '%d-%m-%Y %H:%M:%S')
remainingDays=str(remainingDateTime).split()[0]
remainingTime=str(remainingDateTime).split()[2]
remainingHours=remainingTime.split(':')[0]
remainingMinutes=remainingTime.split(':')[1]
remainingSeconds=remainingTime.split(':')[2]
print(f"Sınavınız için kalan süre: {remainingDays} gün, {remainingHours} saat, {remainingMinutes} dakika, {remainingSeconds} saniye.")