#1- sayilar lsitesini while ile ekrana yazdırın.
# sayilar = [1,3,5,7,9,12,19,21]
# x = len(sayilar)
# y = 0
# while y < x:
#     print(sayilar[y])
#     y += 1

#2- Başlanıç ve bitiş değerlerini kullanıcdan alıp aradaki tüm tek sayıları ekrana yazdırın.
# basNum = int(input('Başlangıç sayısı giriniz:'))
# sonNum = int(input('Bitiş sayısı giriniz:'))
# if basNum - sonNum < 0:
#     if basNum%2==1:
#         while basNum <= sonNum:
#             print(basNum)
#             basNum += 2
#     else:
#         basNum+=1
#         while basNum <= sonNum:
#             print(basNum) 
#             basNum += 2
# else:
#     if sonNum%2==1:
#         while sonNum <= basNum:
#             print(sonNum)
#             sonNum += 2
#     else:
#         sonNum+=1
#         while sonNum <= basNum:
#             print(sonNum)
#             sonNum += 2

#3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
# x = 100
# while x>0:
#     print(x)
#     x-=1

#4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazıdırın.
# sayilar = []
# counter = 1
# while counter <= 5:
#     input_value = int(input(f'{counter}. sayıyı giriniz:'))
#     sayilar.append(input_value)
#     counter += 1
# sayilar.sort()
# print(sayilar)
# print("Girilen değerler:")
# for i, sayi in enumerate(sayilar, start=1): #enumerate, bir dizi (bu durumda sayilar listesi) üzerinde dolaşırken, her bir öğenin indeksini (i) ve değerini (sayi) almanızı sağlar. start=1 argümanı, indekslerin 1'den başlamasını sağlar (Python'da indeksler genellikle 0'dan başlar, ancak bu durumda 1'den başlıyoruz).
#     print(f"sayi{i}: {sayi}")

#5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın
# *ürün sayısını kullanıcıya sorun
# **dictiınary listesi yapısı (name,price) şeklkinde olsun.
# ***ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
items = []
counter_start = 1
counter_end = int(input('Kaç adet ürün girilecek:'))
if counter_end > counter_start:
    while counter_end >= counter_start:
        item_name = str(input(f'{counter_start}. ürünün adını girin:'))
        item_price = float(input(f'{counter_start}. ürünün fiyatını girin:'))
        item ={'name':item_name, 'price':item_price}
        items.append(item)
        counter_start += 1
else:
    print('Yanlış değer girdiniz.')
print('Ürünler:')
for i,x in enumerate(items, start=1):
    print(f"{i}. Ürün Adı: {x['name']}, Fiyatı: {x['price']} TL")