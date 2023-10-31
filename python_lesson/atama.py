x, y, z = 5, 10, 20
#   x = x + 5
x += 5  #   x = x + 5
x -= 5  #   x = x - 5
x *= 5  #   x = x * 5
x /= 5  #   x = x / 5
x += 1
x %= 5  #   x mod5
y = 16
y //= 5 #tam bölme işlemi
y **= 5 # y üzeri 5
print(y)
print(x)

values = 1,2,3,4,5
x,y,*z = values # *z ile kalan elemanların hepsini liste halinde z değişkenine atadık
print(x,y,z)