# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
def repeater(word,sayi):
    while sayi > 0:
        print(f'{word}')
        sayi -= 1
kelime = input('Bir kelime girin:')
kacSefer = int(input('Kelimeniz kaç sefer yazdırılsın:'))
repeater(kelime,kacSefer)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonskiyonu yazınız.
def lister(*params):
    return print(params)
print(lister('mert','salih','mehmet','ali',1,5,7,3+5))
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asalBulucu(beg, end):
    asallarListesi = []
    for sayi in range(beg,end+1):
        if sayi <= 1:
            continue
        if sayi == 2:
            asallarListesi.append(sayi)
            continue
        asalMi = True
        for x in range(2,sayi):
            if (sayi%x == 0):
                asalMi = False
                break
        if asalMi:
            asallarListesi.append(sayi)
    return asallarListesi

beg = int(input("Başlangıç sayısını girin: "))
end = int(input("Bitiş sayısını girin: "))

asallar = asalBulucu(beg, end)
print("Asal Sayılar:", asallar)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.

def tamBolen(sayi):
    tamBolenListesi = []
    for x in range(1,sayi+1):
        if (sayi%x == 0):
            tamBolenListesi.append(x)
    return tamBolenListesi

sayiIn = int(input('Pozitif bir sayı giriniz:'))
bolenler = tamBolen(sayiIn)
print(f'Girdiğiniz sayıyı tam bölen sayılar listesi:{bolenler}')