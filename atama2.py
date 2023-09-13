x,y,z=2,5,10
numbers=1,5,7,10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x y z toplamının farkı nedir.
# sayi1 = float(input("Bir sayı giriniz: "))
# sayi2 = float(input("Bir sayı giriniz: "))
# carpim = sayi1*sayi2
# sonuc = carpim-(x+y+z)
# print(sonuc)

# 2- y'nin x'e kalansız bölümünü hesaplayınız.
# y //= x
# print(y)

# 3- x,y,z toplamının mod 3'ü nedir?
mod = x+y+z
mod %= 3
print(mod)

# 4- y'nin x'inci kuvvetini hesaplayınız.
# y **= x
# print(y)

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
# x,*y,z = numbers
# z **= 3
# print(x,y,z)

# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
x, *y, z = numbers
y_toplam = sum(y)
print(y_toplam)