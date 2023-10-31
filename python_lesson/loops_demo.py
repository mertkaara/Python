'''1-100 arasında rastgele üratilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
* "random modülü" için python random şeklinde arama yapın. (hak = 5)
** 100 üzerinden puanlama yapın. her soru 20 puan
*** hak bilgisini kullanıcıdan alın ve her soru bekşrtşkeb cab sayısı üzerinden hesaplansın.
'''
import random
x = random.random()
rastgeleSayi = int(round(100*x))
hakCount = int(input('Sayıyı kaç hak ile tahmin etmek istersiniz:'))
topHak = hakCount
tahminCount = 0
while hakCount > 0:
    tahmin = int(input('1 ile 100 arasında bir tahmin giriniz:'))
    if tahmin > 0 and tahmin < 101:
        hakCount -= 1
        tahminCount += 1
        if tahmin > rastgeleSayi:
            print('Tahmininiz sayının üzerinde.')
            print(f'Kalan hakkınız:{hakCount}')
            continue
        elif tahmin < rastgeleSayi:
            print('Tahmininiz sayının altında.')
            print(f'Kalan hakkınız:{hakCount}')
            continue
        elif tahmin == rastgeleSayi:
            print('Tebrikler bildiniz.')
            print(f'Puanınız:{100-((100/topHak)*tahminCount)}')
            break
    else:
        print('1 ile 100 arasında bir tahmin giriniz:')
        continue
if hakCount == 0:
    print('Hakkınız doldu :(')
    