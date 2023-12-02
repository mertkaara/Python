# Seviye 1 için:
rfM = 400
rfK = 120
rfD = 200
seviye = 1
counter = 11

toplamM = []
toplamK = []
toplamD = []

while counter > 1:
    print(f"Seviye {seviye} için:\nMetal: {rfM}\nKristal: {rfK}\nDeu: {rfD}")
    print("*****************************************************")
    seviye = seviye + 1
    toplamM.append(rfM)
    toplamK.append(rfK)
    toplamD.append(rfD)
    rfM = rfM*2
    rfK = rfK*2
    rfD = rfD*2
    counter = counter -1

print(f"Toplam metal : {sum(toplamM)}")
print(f"Toplam kristal : {sum(toplamK)}")
print(f"Toplam deu : {sum(toplamD)}")