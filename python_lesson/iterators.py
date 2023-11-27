liste = [1,2,3,4,5]

# for i in liste:
#     print(i)
    
# print(dir(liste))   # Bu objenin metodlarından biri __iter__ yani bu iterable bir obje

iterator = iter(liste)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))   # Burada liste bittiği için StopIteration hatası alırız

# for döngüsünün arka planı:
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break