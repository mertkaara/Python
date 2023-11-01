# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), sleep()

#Student(Person), Teacher(Person) student ve teacher person özelliklerini ve methodlarını miras alır
#Student ve teacher aynı zamanda birer persondur ama studenta özel attributeslar ve methodlar alabilir.add()

class Person():
    def __init__(self0,fname,lname):
        self0.firtName = fname
        self0.lastName = lname
        print('Person created.')
    
    def who_am_i(self0):
        print('I am a Person')
        
class Student(Person):
    def __init__(self1, fname, lname, number):
        Person.__init__(self1,fname,lname)
        self1.studentNumber = number
        print('Student created.')
    def sayHello(self1):
        print('Hello I am a student.')
        
class Teacher(Person):
    def __init__(self2,fname,lname,branch):
        super().__init__(fname,lname) #19. satırdaki ile aynı işlevi gören bir metod
        self2.branch = branch
    def who_am_i(self2): #Override, 14. satırdaki Person classı ile aynı isimli method ama teacher için çağırıldığında bu metod kullanılır.
        print(f'I am a {self2.branch} Teacher.')  
    
p1 = Person('Ali','Yılmaz')
s1 = Student('Mehmet','Kara',191)
t1 = Teacher('Tuncay','Tosun','Math')

print(p1.firtName+' '+p1.lastName)
print(f'{s1.firtName} {s1.lastName}, Number:{s1.studentNumber}') #Stundent classı için __init__ metodu içinde firsName ve lastName değişkenleri tanımlanmamasına rağmen Person classından miras alınıp tanımlandı.
print(f'{t1.firtName} {t1.lastName}')

t1.who_am_i()
p1.who_am_i()
s1.who_am_i() #Student classı için who_am_i metodu tanımlanmamasına rağmen Person classından miras almıştır.
s1.sayHello()