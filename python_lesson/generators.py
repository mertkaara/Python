import time
def cube():
    result = []
    
    for i in range(5):
        result.append(i**3)
    return result

print(cube())
""" Yukarıdaki bu yapıda sayıların küpünü yazırmak istiyoruz ancak bunu bir listeye ekleyerek
    yapıyoruz ve bu da ramde yer kaplıyor. Bunu bellek üzerinde yer kullanmadan generator 
    ile yapabiliriz.
"""
def cube2():
    for i in range(5):
        yield i**3  # yield bize iterable bir obje döndürür

print(cube2())      # generator object     
# bu iterable objenin değerlerini sırasıyla yazdırabiliriz.

for i in cube2():
    time.sleep(0.02)    # Bunu şekil olsun diye koydum
    print(i)
    
##################################################

listem = [i**3 for i in range(5)]
print(listem)

listem1 = (i**3 for i in range(5))  # Generator Object!!
print(listem1)

for i in listem1:
    print(i)
