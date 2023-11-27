
# def usalma(number):
   
#     def inner(power):
#         return number ** power
    
#     return inner

# taban = int(input("Üssü alınacak sayıyı giriniz:"))
# us = int(input("Üssü giriniz:"))

# islem = usalma(taban)
# print(islem(us))

def islem(islem_adi):
    
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    else:
        return carpim
    
toplama = islem("toplama")
print(toplama(1,3,5,7))

carpma = islem("carpim")
print(carpma(1,2,3,4,5))