
class Circle:
    #Class object attribute
    pi = 3.14
    def __init__(self,r=1):
        self.r = r
    #Methods
    def cevre_hesapla(self):
        return 2*self.pi*self.r
    def alan_hesapla(self):
        return self.pi * (self.r**2)
    
r1 = float(input('Çember yarıçapı giriniz: '))
c1 = Circle(r1)
print(f'Çemberin çevresi: {c1.cevre_hesapla()} \nÇemberin alanı: {c1.alan_hesapla()}')