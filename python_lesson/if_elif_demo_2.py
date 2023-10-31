#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# sayi = float(input('Bir sayı giriniz:'))
# if sayi > 0 and sayi <= 100:
#     print('Sayınız 0 ve 100 aralığındadır.')
# else:
#     print('Sayınız 0 ve 100 aralığında değildir.')

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# sayi = int(input('Bir sayı giriniz:'))
# if sayi > 0 and sayi %2 == 0:
#     print('Sayınız sıfırdan büyük ve çifttir.')
# elif sayi > 0 and not sayi %2 == 0:
#     print('Sayınız sıfırdan büyük ancak çift değildir.')
# elif sayi <= 0 and sayi %2 == 0:
#     print('Sayınız sıfırdan büyük değildir ancak çifttir.')
# else:
#     print('Sayınız sıfırdan büyük ve çift değildir.')

#3- Email ve parola bilgileri ile giriş kontrolü yapınız.
# email = 'mertkara1995@gmail.com'
# password = 'abc123'
# inputEmail = input('Email:')
# inputPassword = input('Password:')
# if email == inputEmail and password == inputPassword:
#     print('Girdiniz.')
# elif email == inputEmail and not password == inputPassword:
#     print('Şifreniz yanlış.')
# elif not email == inputEmail and password == inputPassword:
#     print('Email adresiniz yanlış.')
# else:
#     print('Email adresiniz ve parolanız yanlış.')

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# list = [a,b,c]
# list.sort(reverse=True)
# print(f"En büyük sayı {list[0]}, ikinci {list[1]} ve üçüncü {list[2]}.")

# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# variables = {'a': a, 'b': b, 'c': c}

# # Sözlükteki değişken adlarını ve değerlerini görüntüle
# for var_name, var_value in variables.items():
#     print(f"{var_name} değişkeninin değeri: {var_value}")

# # Büyükten küçüğe sıralanmış liste oluştur
# sorted_list = sorted(variables.items(), key=lambda x: x[1], reverse=True)
# print(f"En büyük sayı {sorted_list[0][0]}, ikinci {sorted_list[1][0]} ve üçüncü {sorted_list[2][0]}.")
# print(sorted_list)

#5- Kullanıcıdan 2 vize (%60) ve final %40 notunu alıp ortalama hesaplayınız.
#Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazıdırn.
#a) ortalama olsa bile final notu en az 50 olmalıdır.
#b) finalden 70 alındığında ortalamanın önemi olmasın.
# vize1 = int(input('Birinci vize notunuzu giriniz:'))
# vize2 = int(input('İkinci vize notunuzu giriniz:'))
# final = int(input('Final notunuzu giriniz:'))
# ortalama = (vize1*0.3)+(vize2*0.3)+(final*0.4)
# ortalama = round(ortalama)
# print(f'Ortalamanız:{ortalama}')
# if ortalama >= 50 and final >= 50:
#     print('Geçtiniz.')
# elif ortalama < 50 and final >= 70:
#     print('Geçtiniz.')
# else:
#     print('Galdınız.')

#6- Kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız.
# formül = (kilo / boyun karesi)
# 0 - 18.4 zayıf
# 18.5 - 24.9 normal
# 25.0 - 29.9 kilolu
# 30 - 34.9 şüşko
# > 35 sıkıntılı
kg = float(input('Ağırlığınızı kg cinsinden giriniz:'))
boy = float(input('Boyunuzu metre cinsinden giriniz:'))
index = kg / boy**2
print(index)
if index > 0 and index < 18.5:
    print('Zayıfsınız.')
elif index >= 18.5 and index < 24.5:
    print('Kilonuz normal.')
elif index >= 24.5 and index < 30:
    print('Kilolusun.')
elif index >= 30 and index < 34.5:
    print('Obezsiniz.')
elif index >= 34.5:
    print('Sağlığınız ciddi tehlikede!!!')
else:
    print('Girdiğin değerler sıkıntılı hacı.')