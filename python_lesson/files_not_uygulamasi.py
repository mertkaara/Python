
def not_hesapla(satir):
    satir = satir[:-1]
    listem = satir.split(':')
    ogrenciAdi = listem[0]
    
    notlar = listem[1].split(',')
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortlama = (not1+not2+not3)/3
    ortlama = str(ortlama)
    return 'Öğrenci adı:'+ogrenciAdi+'\nNot ortalaması:'+ortlama+'\n'

def oralamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input("Öğrenci adı:")
    soyad = input("Öğrenci soyadı:")
    not1 = input("Not1:")
    not2 = input("Not2:")
    not3 = input("Not3:")
    
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')

def notlari_kaydet():
    with open('sinav_notlari.txt',"r",encoding="utf-8") as file:
        listem1 = []
        
        for i in file:
            listem1.append(not_hesapla(i))
            
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in listem1:
                file2.write(i)
        
while True:
    islem = input('1- Notları Oku\n2- Not gir\n3- Notları kaydet\n4- Çıkış\n')
    
    if islem == '1':
        oralamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    else:
        break