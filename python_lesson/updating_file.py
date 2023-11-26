
# with open("newfile.txt","r+", encoding="utf-8") as file:    # r+ parametresi hem okuma hem yazma modunu temsil eder.
#     print(file.read())
    
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.write("deneme")    # 0. konumdan itibaren deneme yazar, yazdırılan metnin boyunda önceden o indexlerde var olan metni siler yerine yeni yazdığımızı getirir.
    
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

#********** Sayfa sonunda güncelleme  **********   
# with open("newfile.txt","a", encoding="utf-8") as file: # a (append) ile açarsak eklemeyi en sona yaparız.
#     file.write("\nMert KARA update")
    
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())
    
#********** Sayfa başında güncelleme  **********

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Mert KARA başa ekleme\n" + content   #henüz dosya içerisine aktarılmadı
#     #Dosya içerisine aktarmak için:
#     file.seek(0)    #Cursosr 0. indexte
#     file.write(content)
    
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())
    
#********** Sayfa ortasında güncelleme  **********
with open("newfile.txt","r+", encoding="utf-8") as file:
    listem = file.readlines()   #readlines fonksiyonu içeriği listeye çevirir.
    #listeden ekleme yapmak istediğimiz indexi tespit ederiz.
    help(listem.insert) # Verilen indexin öncesine ekleme yapar
    listem.insert(3,"Mert KARA ortaya ekleme writelines\n")
    file.seek(0)
    # for i in listem:    #Oluşturduğumuz listeyi for döngüzü ile dosyaya geri yazdırıyoruz.
    #     file.write(i)
    #Kullandığımız bu for döngüsü yerine .writelines metodu ile listeyi direkt dosyaya çevirebiliriz:
    file.writelines(listem)
        
        
with open("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())