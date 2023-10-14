# # Global scope
# x = 'Global x'

# def function():
#     # Local scope
#     x = 'Local x'
#     print(x)

# function()
# print(x)



name = 'global string'
def greeting():
    name = 'Mert' #Bunu da yorum satırı yaparsak 'global string' yazar
    
    def hello():
        name = 'Nilgün' #En içteki bu olduğu için çalıştırınca Nilgün yazar. Bunu yorum satırı yaparsak bir önceki tanımı yani 'Mert' yazar
        print(f'Hello {name}')

    hello()

greeting()



x = 50
def test():
    global x
    print(f'x: {x}')
    x = 100
    print(f'x is changed to: {x}')

test()
print(x)