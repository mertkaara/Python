# error

# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError

# error handling

# try:
#     x = int(input('x:'))
#     y = int(input('y:'))
#     print(x/y)
# except ZeroDivisionError:
#     print('y için "0" girilemez.')
# except ValueError:
#     print('x ve y sayı olmalıdır.')

# try:
#     x = int(input('x:'))
#     y = int(input('y:'))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz')
#     print(e)

while True:
    try:
        x = int(input('x:'))
        y = int(input('y:'))
        print(x/y)
    except:
        print('Yanlış bilgi girdiniz.')
    else:       # except çalışmadığı zaman else kısmına geçilir ve döngüden çıkılır
        break 
    finally:
        print('try except sonlandı.')