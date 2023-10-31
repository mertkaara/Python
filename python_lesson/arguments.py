def changeName(n):
    n = 'ada'
name = 'yiğit'
changeName(name)
print(name)
'''
Bu kodda name değişkeni değişmedi çünkü Python'da değişkenlerin fonksiyonlara parametre olarak geçirilmesi ve bu fonksiyonlar içinde değiştirilmesi, yerel bir kopya oluşturur ve orijinal değişkeni etkilemez.
İşte kodun adım adım açıklaması:
name adında bir değişken oluşturulur ve "yiğit" değeri atanır.
changeName adında bir işlev (fonksiyon) tanımlanır ve bu işlev n adında bir parametre alır.
İşlev içinde, n değişkenine "ada" değeri atanır.
changeName(name) kodu çağrıldığında, name değişkeni changeName işlevine parametre olarak geçirilir. Ancak, bu işlem sırasında name'in kopyası olan n adındaki yerel bir değişken oluşturulur ve bu n değişkenine "ada" atanır.
Son olarak, print(name) ifadesi ile orijinal name değişkeni ekrana yazdırılır ve bu, "yiğit" olarak görüntülenir. Çünkü işlev içinde yapılan değişiklik, orijinal name değişkenini etkilemez.
Değişkenlerin işlevler arasında paylaşılması için işlev içinde değişkenin global olması veya değişkenin referansını (örneğin bir liste veya sözlük gibi değiştirilebilir bir nesne) iletmek gereklidir.
'''
def change(n):
    n[0] = 'istanbul'
sehirler = ['ankara','izmir']
n = sehirler[:] #slicing, şehirler listesini n değişkenine kopyaladı
print(sehirler)
print(n)
change(n)
print(sehirler)
print(n)

def add1(a,b):
    return sum((a,b))
print(add1(12,42))

def add(*params): # tek * tuple listesi oluşturur
    print(params)
    # print(type(params)) # class Tuple listesi
    return sum((params))
print(add(10,15,22,31,45))
print(add(10,20,3))

def displayUser(**args): # çift ** dictionary oluşturur.
    for key,value in args.items():
        print(f'{key} is {value}')
        # print(type(args)) # class dictionary
displayUser(name='Mert', surname ='KARA', age=27, city='Denizli')
displayUser(name='Ali', surname='KESKİN', age=32, city='Ankara', phone='053185454')

def myFunc(a, b, *args1, **kwargs):
    print(a)
    print(b)
    print(args1)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, key1='value1', key2='value2')