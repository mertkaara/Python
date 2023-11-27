""" Bir fonksiyonun öncesinde, sonrasında veya hem öncesi hem sonrasında
    bazı işlemleri yaptırmask istiyorsak ancak bu işlemleri o fonksiyonun
    içerisine dahil etmek istemiyorsa ayrı bir fonksiyon içerisinde çalıştırılmasını
    istiyorsak bu yöntemi kullanabiliriz.
"""
# def my_decorator(func):
#     def wrapper(name1):
#         print("Fonksiyondan önceki işlemler..")
#         func(name1)
#         print("Fonksiyondan sonraki işlemler..")
#     return wrapper

# def sayHello():
#     print("Hello!")

# @my_decorator    
# def sayGreeting(name):
#     print("Greetings!",name)
    
# # sayHello = my_decorator(sayHello)

# # sayHello()
# sayGreeting("Mert")

import math
import time

# def usalma(a,b):
#     start = time.time()
#     time.sleep(1)
    
#     print(math.pow(a,b))
    
#     end = time.time()
#     print("Fonksiyon "+ str(end-start)+" saniyede hesaplandı.")
    
# usalma(3,2)


def decorator(func):
    def zaman_hesaplayici(num):
        start = time.time()
        time.sleep(1)
        func(num)
        end = time.time()
        print("Fonksiyon "+ str(end-start)+" saniyede hesaplandı.")
    return zaman_hesaplayici

@decorator      #decorator söz dizimi
def faktoriyel(num):
    print(math.factorial(num))
    
faktoriyel(5)