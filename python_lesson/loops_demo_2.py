import random

rastgeleSayi = random.randint(1, 100)
hakCount = int(input('Sayıyı kaç hak ile tahmin etmek istersiniz:'))
topHak = hakCount  # topHak'ı tanımladık
tahminCount = 0

while hakCount > 0:
    tahmin = int(input(f'1 ile 100 arasında bir tahmin giriniz ({hakCount} hakkınız kaldı):'))

    if 1 <= tahmin <= 100:
        tahminCount += 1
        hakCount -= 1

        if tahmin > rastgeleSayi:
            print('Tahmininiz sayının üzerinde.')
        elif tahmin < rastgeleSayi:
            print('Tahmininiz sayının altında.')
        else:
            puan = 100 - (100 / topHak * tahminCount)
            print(f'Tebrikler, doğru tahmin! Puanınız: {puan:.2f}')
            break
    else:
        print('1 ile 100 arasında bir tahmin giriniz.')

if hakCount == 0:
    print('Hakkınız doldu. Sayı:', rastgeleSayi)
