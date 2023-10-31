# 1-100 e kadar sayıları yazdır
x = 0
while x <= 100:
    print(x)
    x += 1

name = '' #False
while not name.strip():
    name = input('İsminizi giriniz:')
print(f'Merhaba, {name}')