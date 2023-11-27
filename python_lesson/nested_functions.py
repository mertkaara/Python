""" İç içe fonksiyonlar """

def greeting(name):
    print('Hello',name)
    
print(greeting('Mert'))

sayHello = greeting

print(sayHello)     # sayHello ve greeting in ram adresleri aynı burada eşitleme yaparken değişkenleri birbirine eşitlemek yerine var olan değişkenin ram adresine yönlendirme yapılır
print(greeting)

del sayHello        # sayHello değişkeni silinse dahi greeting fonskiyonu kullanılmaya devam edilebilir.
print(greeting)

# Encapsulation
def outer(num1):
    print("Outer")
    def inner_increment(num1):
        print("Inner")
        return num1 +1
    num2 = inner_increment(num1)
    #inner_increment(num1)
    print(num1,num2)
  
outer(10)
# inner_increment(10) # inner_increment fonksiyonu bu şekilde kullanılamaz, bu fonksiyon sadece outer fonksiyonu içerisinde tanımlıdır.

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer.")
    if not number >= 0:
        raise ValueError("number must be zero or greater than zero.")
    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)
    return inner_factorial(number)

try:
    print(factorial("5"))
except Exception as ex:
    print(ex)