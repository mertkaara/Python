def square(num): return num**2

numbers = [1,3,5,9,4,10,12]

result = list(map(square,numbers)) # Liste metodu uygulanmadan map metodundan çıktı alırsak ram üzerinde bir adres ile geri döner.

result1 = list(map(lambda num: num**2,numbers)) # Lambda expression, eğer yapacağımız işlem için bir fonksiyon tanımlamak istemiyorsak tek seferlik bir işlem yapılacaksa kullanabiliriz.

kare = lambda num: num**2

print(list(map(kare,numbers)))
print(result)
print(result1)


def check_even(num):
    return num%2==0
result2 = list(filter(check_even,numbers))
result3 = list(filter(lambda num: num%2==0,numbers))
print(result2)
print(result3)