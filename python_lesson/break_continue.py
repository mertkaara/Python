name = 'Mert KARA'
# for letter in name:
#     if letter == 'r':
#         break #Döngüden çıkış yapılır
#     print(letter)
# for letter in name:
#     if letter == 'r':
#         continue # 'r' harfini yazırmadan döngüye devam eder
#     print(letter)
# x = 0
# while x<5:
#     if x == 2:
#         continue # Continue den sonra kod okuma başa döndüğü için x+=1 satırı uygulanmaz bu yüzden x==2 de kalır.
#     print(x)
#     x+=1
#1-100 e kadar tek sayıların toplamı.
x = 0
result = 0
while x <= 100:
    x+=1
    if x%2 == 0:
        continue
    result += x
print(f'Toplam:{result}')