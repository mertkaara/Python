import os
import datetime

result = dir(os)

# os.chdir('C:\\')    # Dizini değiştirir
# os.chdir('..')    # Bir önceki dizine geçme

result = os.getcwd()    # Etkin dizinini yazdırır

# os.mkdir("yeni_klasor") # Mevcut dizine klasör oluşturur
# os.makedirs("newdirectory/yeniklasor")  # İç içe klasörler oluşturma
# os.rename("yeniklasor","kodlarım")  # yeniklasör isimli dosyayının ismini kodlarım olarak değiştirir

result = os.listdir()   # Mevcut dizini listeler
# result = os.listdir("C:\\") # C dizini altındakileri listeler

# for dosya in os.listdir():    # Mevcut dizindeki sonu .txt ile biten dosyaları yazdırır
#     if dosya.endswith('.txt'):
#         print(dosya)

# result = os.stat("sinav_notlari.txt")   # Dosya bilgilerini yazdırır
# result = datetime.datetime.fromtimestamp(result.st_ctime)   # Dosyanın oluşturulma zamanı

# os.system("notepad.exe")    # Sistem üzerinden istediğimiz bir programı çalıştırabiliriz.

result = os.path.abspath("sonuclar.txt")    # Dosya isminde tam dizin adresini alırız
result = os.path.dirname("C:/Users/Mert/Desktop/Python/sonuclar.txt")   # Dosya ismini dizinden çıkarır dosyanın içinde bulunduğu klasörün dizini
result = os.path.exists("sonuclar.txt") # Mevcut konumda bu dosya var mı? True/False döndürür
result = os.path.isdir("C:/Users/Mert/Desktop/Python")  # Bu dizin bir klasör mü? True/False
result = os.path.isfile("C:/Users/Mert/Desktop/Python") # Bu dizin bir dosya mı? True/False
result = os.path.join("C:\\","deneme","deneme1")    # Dizin oluşturur (Not: klasör ya da dosya oluşturmaz sadece dizin adresini oluşturur)
result = os.path.split("C:\\deneme")    # Dizini liste şeklinde ayırır
result = os.path.splitext("sonuclar.txt")   # Dosyanın ismi ile uzantısını ayırır liste olarak verir

print(result)