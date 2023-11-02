myList = [1,2,3]
myString = 'my string'

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

class Movie():
    
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
    
    def __str__(self):
        return f"{self.title} by {self.director}" # str metodunu tanımladığımız için m objesini print(str(m)) ile yazdırdığımızda bu metoda göre ekrana yazdırılır.
    
    def __len__(self):  # len metodunu tanımladığımız için m objesinde len metodu çalıştırıldığında tanımladığımız değer yazdırılacak
        return self.duration

    def __del__(self):
        print('Film objesi silindi.')
        
m = Movie('film adı','yönetmen adı',120)

# print(type(m))
# print(len(m))   #Bu method Movie classına tanımlanmadığı için çalışmaz

print(str(myList))
print(str(m))
print(len(myList))
print(len(m))       # __len__ metodunda self.duration değişkenini sonuç olarak döndürdüğümüz için bu metod kullanıldığında belirttiğimiz değer yazdıralacak.

del m

print(m)