# x = 10

# if x >5:
#     raise Exception("x 5'ten büyük değer alamaz.")

def check_password(psw):
    import re   # Regular Expression
    if len(psw) < 8:
        raise Exception("Parolanız en 8 karakterli olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam içermelidir.")
    elif re.search("\s",psw):      # Regular expression boşluk karakteri.
        raise Exception("Parola boşluk içermemelidir.")

    
password = "12345678aB"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Parolanız oluşturuldu.")
    
class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception('Name alanı fazla karakter içeriyor, 10 karakterden büyük olamaz.')
        else:
            self.name = name

p = Person('Mertttttttt',1995)