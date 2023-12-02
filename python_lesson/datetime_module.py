from datetime import datetime
from datetime import timedelta

simdi = datetime.today()
result = simdi.hour
result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%y')
result = datetime.strftime(simdi,'%x')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%a')
result = datetime.strftime(simdi,'%b')
result = datetime.strftime(simdi,'%y %b %a')

# t = '28 Kasım 2023'
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

# print(simdi)
# print(result)

t = '28 November 2023 hour 14:12:34'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(dt)

birthday = datetime(1995,10,12)
print(birthday)
result = datetime.timestamp(birthday)   # Saniye bilgisi verir
result = datetime.fromtimestamp(result) # Saniye bilgisinden tekrar datetime'a çevirir
result = simdi - birthday   # timedelta objesi
result = simdi + timedelta(days=10)

print(result)