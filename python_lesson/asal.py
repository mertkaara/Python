'''
Girilen bir sayının asal olup olmadığını bulun.
'''
girdi = int(input('Bir sayı giriniz:'))
asalmi = True
if girdi == 2:
    print(f'Sayınız {girdi} asaldır.')
if girdi <= 1:
    asalmi = False

for x in range(2,girdi):
    if (girdi % x == 0):
        asalmi = False
        break

if asalmi:
    print(f'Sayınız {girdi} asaldır.')
else:
    print(f'Sayınız {girdi} asal değildir.')