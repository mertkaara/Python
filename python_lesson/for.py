sayilar = [1,4,7,10,13]
for i,sayi in enumerate(sayilar, start=1): #enumerate, bir dizi (bu durumda sayilar listesi) üzerinde dolaşırken, her bir öğenin indeksini (i) ve değerini (sayi) almanızı sağlar.
    print(f'{i}. sayı:{sayi}')

# name = 'Mert KARA'
# for n in name:
#     print(n)

# tuple = [(1,2),(1,3),(3,5),(5,7)]
# for a,b in tuple:
#     print(a,b)

# d = {'k1':1, 'k2':2, 'k3':3}
# for x,y in d.items():
#     print(x)