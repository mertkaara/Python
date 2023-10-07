import math
# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip, ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma 
#    koşulunu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
# name = input('İsminizi giriniz:')
# age = int(input('Yaşınızı giriniz:'))
# school = input('En mezun olduğunuz okul:')
# isSchool = (school == 'lise') or (school == 'üniversite')
# print(school)
# print(isSchool)
# if age <= 18:
#     if isSchool == True:
#         print(f'Sayın {name}, ehliyet alabilirsiniz.')
#     else:
#         print(f'Sayın {name}, en az lise mezunu olmanız lazım.')
# else:
#     print(f'Sayın {name}, 18 yaşından büyük olmanız lazım.')


# 2- Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre
# 0 - 24 > 0
# 25- 44 > 1
# 45- 54 > 2
# 55- 69 > 3
# 70- 84 > 4
# 85- 100 > 5
yazili1 = float(input('İlk yazılı puanınızı giriniz:'))
yazili2 = float(input('İkinci yazılı puanınızı giriniz:'))
sozlu = float(input('Sözlü puanınızı giriniz:'))
ortalama = (yazili1 + yazili2 + sozlu ) / 3
ortalamaRound = round(ortalama)

if ortalama <= 100:
    print(f'Ortalamanız:{ortalamaRound}')
else:
    print('Yanlış puan girdiniz.')

if (0 <= ortalamaRound <= 24) :
    print('Notunuz: 0')
elif (25 <= ortalamaRound <= 44):
    print('Notunuz: 1')
elif (45 <= ortalamaRound <= 54):
    print('Notunuz: 2')
elif 55 <= ortalamaRound <= 69:
    print('Notunuz: 3')
elif 70 <= ortalamaRound <= 84:
    print('Notunuz: 4')
elif 85 <= ortalamaRound <= 100:
    print('Notunuz: 5')
else:
    print('Yanlış puan girdiniz.')

#3 Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1. bakım  1 yıl
# 2. bakım  2. yıl
# 3. bakım  3. yıl
# *Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# ** datetime modülünü kullanmanız gerekiyor.

