# Girilen bir sayının 0-100 aralığından olup olmadığını kontrol edin.
#a = int(input("Bir sayı giriniz:"))
#result = (a >= 0) and (a <= 100)
# Girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin.
#result = (a > 0) and (a %2 == 0)
# e-mail ve parola bilgileri ile giriş kontrolü yapınız
user_Mail = "mertkara1995@gmail.com"
user_Pass = "123456"
#in_Mail = str(input("mail adresinizi giriniz:"))
#in_Pass = str(input("Parolanızı giriniz:"))
#result = (in_Mail == user_Mail) and (in_Pass == user_Pass)
# kişinin kilo boy bilgilerini alıp kilo indeksini hesaplayınız
boy = float(input("Metre cinsinden boyunuzu giriniz:"))
kilo = float(input("Kilogram cinsinden boyunuzu giriniz:"))
result = ( kilo / boy**2)
print(f"Boy kilo indeksiniz:{result}")