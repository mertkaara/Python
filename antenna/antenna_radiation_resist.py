import math
cevre = 0.1
a = cevre / (2 * math.pi)
b = 0.0001
frekans = 300e6
mu_0 = 4 * math.pi * 1e-7
iletkenlik = 5.7 * 1e7
c = 3* 1e8
s = math.pi * a**2
dalga_boyu = c / frekans
k = ( 2 * math.pi ) / dalga_boyu
Rr = 120 * math.pi * ((2 * math.pi) / 3) * ((k * s) / dalga_boyu)**2
print(f"Işıma direnci:{Rr} Ohm")
sayi = (2 * math.pi * frekans * mu_0) / (2 * iletkenlik)
karekok = math.sqrt(sayi)
rL = (a/b)*karekok
print(f"Antenin kayıp direnci:{rL} Ohm")
ecd = (Rr / (Rr + rL))
yuzde_ecd = ecd*100
print(f"Hesaplanan verimlilik:{ecd}, yüzde verimlilik:%{yuzde_ecd}")