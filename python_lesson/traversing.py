
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(7)  #sadece ilk 7 karakteri okur
    print(content)
    file.seek(15)           #cursorun konumunu belirtilen yere gönderir.
    print(file.tell())      #cursorun konumunu verir.
    content2 = file.read()
    print(content2)

#file.close() artık file.close fonksiyonuna ihtiyacımız yok çünkü,
#with ile oluşturduğumuz kod bloğunun sonuna gelindiğinde dosya kapanacak.