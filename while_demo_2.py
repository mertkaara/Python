items = []

# Kullanıcıdan geçerli bir ürün sayısı girişi alın
while True:
    try:
        counter_end = int(input('Kaç adet ürün girilecek: '))
        if counter_end > 0:
            break
        else:
            print('Lütfen pozitif bir değer girin.')
    except ValueError:
        print('Geçerli bir sayı girin.')

counter_start = 1

# Ürünleri alın ve dictionary'ye ekleyin
while counter_start <= counter_end:
    item_name = input(f'{counter_start}. ürünün adını girin: ')
    item_price = None
    
    while item_price is None:
        try:
            item_price = float(input(f'{counter_start}. ürünün fiyatını girin: '))
        except ValueError:
            print('Geçerli bir fiyat girin.')
    
    item = {'name': item_name, 'price': item_price}
    items.append(item)
    counter_start += 1

print('Ürünler:')
for i, x in enumerate(items, start=1):
    print(f"{i}. Ürün Adı: {x['name']}, Fiyatı: {x['price']} TL")
