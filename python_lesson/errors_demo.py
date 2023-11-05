# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
liste = ["a1b","1","2","5a","10b","abc","10","50"]
liste1 = []
x=-1
for a in liste:
    x += 1
    try:
        int(a)
        liste1.append(a)
    except ValueError:
        print(f'Index number {x} is broken.')
print(liste1)
# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz
# aksi halde hata mesajı yazdırın.
while True:
    sayi = input('Sayı: ')
    if sayi == 'q':
        break
    try:
        result = float(sayi)
        print(f'Girdiğiniz sayı: {result}')
    except ValueError:
        print('Geçersiz sayı.')
        continue
# 3: Girilen parola içinde türkçe karakter varsa hata mesajı yazdırın.
def checkPassword(password):
    turkce_chars = 'ğüşöçıİ'
    for i in password:
        if i in turkce_chars:
            raise TypeError('Parola türkçe karakter içeremez.')
    else:
        pass
    print('Parolanız geçerli.')
parola = input('Bir parola giriniz:')
checkPassword(parola)
# 4: Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
#(sayısal bir değer değilse veya negatifse)
from math import factorial
def checkFactorial(x):
    try:
        x = int(x)  # Girdiyi tam sayıya dönüştür
        if x <= 0:
            raise ValueError('Girdiğiniz sayı sıfırdan büyük olmalıdır.')
        result = factorial(x)  # Faktoriyel hesaplamasının sonucunu sakla
        print(f'{x} faktoriyeli = {result}')
    except ValueError:
        print('Girdiğiniz sayı geçersiz.')
sayi = input('Bir sayı giriniz:')
checkFactorial(sayi)