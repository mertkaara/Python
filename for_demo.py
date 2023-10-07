sayilar = [1,3,5,7,9,12,19,21]
# #1- Sayılar listesindeki hangi sayılar 3'ün katıdır?
# for sayi in sayilar:
#     if (sayi%3==0):
#         print(sayi)
# #2- Sayılar listesinde sayıların toplamı kaçtır?
# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print('toplam:',toplam)
# #3- Sayılar listesindeki tek sayıların karesini alınız.
# for sayi in sayilar:
#     if not sayi %2==0:
#         print(sayi**2)
sehirler = ['kocaeli','istabul','ankara','izmir','rize']
# #4- Şehirlerden hangileri en fazla 5 karakterlidir?
# for sehir in sehirler:
#     a = len(sehir)
#     if a <= 5:
#         print(sehir)
urunler = [
    {'name':'samsung S6', 'price': '3000'},
    {'name':'samsung S7', 'price': '4000'},
    {'name':'samsung S8', 'price': '5000'},
    {'name':'samsung S9', 'price': '6000'},
    {'name':'samsung S10', 'price': '7000'}
]
# #5- Ürünlerin fiyatları toplamı nedir?
# toplam = 0
# for urun in urunler:
#     toplam += int(urun['price'])
# print(f'Toplam fiyat:{toplam}')
#6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?
for urun in urunler:
    a = int(urun['price'])
    if a <= 5000:
        print(urun['name'])