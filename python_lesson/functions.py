def sayHello(name = 'user'): # varsayılan parametre belirtmeseydik fonksiyona değer girmeden çağırdığımızda hata alırdık.
    print(f'Hello {name}')

sayHello('Mert')
sayHello('Nilgün')
sayHello() #Parametre göndermediğimizde varsayılan yazılır.

def total(num1, num2):
    return num1 + num2

result = total(11,25)
print(result)

def total1(num1, num2):
    print(num1+num2)

total1(18,7)

def yasHesapla(dogumYili):
    return 2023 - dogumYili

userDogumYili = int(input('Doğum yılınızı giriniz:'))
ageUser = yasHesapla(userDogumYili)
print(f'Yaşınız:{ageUser}')
isim = input('İsminizi giriniz:')

def emekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı.
    INPUT: Doğum yılı ve isim.
    OUTPUT: Hesaplanan yıl bilgisi.
    '''
    emeklilik = 65 - ageUser
    if emeklilik > 0:
        print(f'Sayın {isim}, emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print(f'Sayın {isim}, zaten emekli oldunuz.')

emekliligeKacYilKaldi(ageUser,isim)

print(help(emekliligeKacYilKaldi))