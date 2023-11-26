# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu: dosyayi hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur. Bu modda önceki bilgiler silinir.
# file = open('newfile.txt','w')
# file1 = open('C:/users/mert/desktop/newfile.txt','w')
# file.close()
# file = open('newfile.txt','w',encoding='utf-8')
# file.write('Mert KARA')
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur. Bu modda yazılanlar önceki bilgilerin üzerine eklenir.
# file = open('newfile.txt','a',encoding='utf-8')
# file.write('Mert KARA\n')
# file.close

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open('newfile.txt','x',encoding='utf-8')

# "r": (Read) okuma. Varsayılan. Dosya konumda yoksa hata verir.
# try:
#     file = open('newfile.txt','r')
#     print(file)
# except FileNotFoundError:
#     print('Dosya okuma hatası.')
# finally:
#     file.close()

file = open('newfile.txt','r',encoding='utf-8')

# for döngüsü
# for i in file:
#     print(i,end='') # Sadece print ile yazdırdığımızda her satır arasında bir boş satır bırakır, end= ifadesi ile onu düzenleyebiliriz.
# file.close

# read fonskiyonu
# content1 = file.read()
# print('Içerik 1')
# print(content1)

# content2 = file.read()
# print('Içerik 2')
# print(content2) # Ekrana bir şey yazdırılamaz çünkü ilk yazdırılışında cursor içeriğin en sonunda kalmıştır ve dosya kapatılmadan tekrar okuma yapıldığı için cursorun okuyacağı bir içerik kalmamıştır.

# readline() fonksiyonu
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# file.close

# readlines() fonksiyonu
liste1 = file.readlines()
print(liste1)
print(liste1[0])
print(liste1[2])
file.close()