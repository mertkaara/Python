# class

class Person:
    # class attributes
    adress = 'no information'
    #constructor (yapıcı metod)
    def __init__(self,name,year):
        # obeject attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
    # methods


# object (instance)
p1 = Person('ali',1990)
p2 = Person(year = 1995, name = 'yağmur')

# updating
p1.name = 'ahmet'
p1.adress = 'kocaeli'

# accessing object attributes
print(f'name: {p1.name}, year: {p1.year}, adress: {p1.adress}')
print(f'name: {p2.name}, year: {p2.year}, adress: {p2.adress}')


print(p1)
print(type(p1))