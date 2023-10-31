MertHesap = {
    'ad': 'Mert KARA',
    'hesapNo': '191949',
    'bakiye' : 3000,
    'ekHesap' : 2000,
    'ekHesapLimit' : 2000
}
AliHesap = {
    'ad': 'Ali KARA',
    'hesapNo': '191950',
    'bakiye' : 2000,
    'ekHesap' : 1000,
    'ekHesapLimit' : 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print(f"{miktar} TL başarıyla çektiniz.")
        kalanBakiye(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        kalan = miktar - hesap['bakiye']
        if (toplam >= miktar):
            ekHesapKullanimi = input(f'Bakiyeniz yetersiz. Ek hesabınızdan {kalan} TL kullanılsın mı?(e/h):')
            if ekHesapKullanimi == 'e':
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= kalan
                print(f"{miktar} TL başarıyla çektiniz.")
                kalanBakiye(hesap)
            else:
                print('Para çekme işleminiz iptal edildi.')
                kalanBakiye(hesap)
        else:
            print('Yetersiz bakiye.')
            kalanBakiye(hesap)

def kalanBakiye(hesap):
    print(f"Hesap bakiyeniz {hesap['bakiye']} TL, ek hesap bakiyeniz {hesap['ekHesap']} TL.")

def paraYatir(hesap,miktar):
    if (hesap['ekHesap'] < hesap['ekHesapLimit']):
        fark = hesap['ekHesapLimit'] - hesap['ekHesap']
        if miktar > fark:
            hesap['ekHesap'] = hesap['ekHesapLimit']
            hesap['bakiye'] += (miktar - fark)
            print('Paranız başarıyla yatarıldı.')
            kalanBakiye(hesap)
        else:
            hesap['ekHesap'] += miktar
            print('Paranız başarıyla yatarıldı.')
            kalanBakiye(hesap)
    else:
        hesap['bakiye'] += miktar
        print('Paranız başarıyla yatarıldı.')
        kalanBakiye(hesap)

        
paraCek(MertHesap,3500)
print('_________________________________')
paraYatir(MertHesap,2800)