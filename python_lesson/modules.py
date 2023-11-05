# importing modules
    # math module

# Yöntem 1
# import math
import math as islem # math modülüne takma ad verir.

# value = dir(math)
# value = help(math)
# value = help(math.factorial)
# value = math.sqrt(49)
# value = math.floor(5.7)
# value = islem.factorial(5) # math modülünü islem olarak kullandık.

# Yöntem 2
# from math import * # math modülünü tamamen alır artık kullanırken math. diye fonksiyonları kullanmamıza gerek yok.
# from math import factorial,ceil,sqrt,log

# value = factorial(5)
# value = sqrt(9)
# value = log(100)

# print(value)
    # random module
import random

# result = dir(random)
# result = help(random)
# result = random.random() # 0.0 - 1.0 
# result = random.uniform(4,20) # Belirlediğimiz aralıkta sayı üretir.
# result = random.randint(20,80) # Belirlediğimiz aralıkta tamsayı üretir.

greeting = 'Hello there.'
names = ['ali','yağmur','deniz','mert','cenk']
# result = names[random.randint(0,len(names)-1)]
result = random.choice(names) # Bir üstteki kod satırında yapılan işlemi yapar.
result = random.choice(greeting)

myList = list(range(10))
random.shuffle(myList)  # Listeyi karıştırır.
myList1 = range(100)

result = random.sample(myList1,3) # Listeden belirttiğimiz kadar rastgele örnek alır.

print(result)