def asal_mi(sayi):
    if sayi <= 1:
        return False
    if sayi <= 3:
        return True

    if sayi % 2 == 0 or sayi % 3 == 0:
        return False

    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return False
        i += 6

    return True

girdi = int(input('Bir sayı giriniz:'))
if asal_mi(girdi):
    print(f'Sayınız {girdi} asaldır.')
else:
    print(f'Sayınız {girdi} asal değildir.')
