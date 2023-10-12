numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

numbers1 = [x for x in range(10)]
print(numbers1)

numbers2 = [x**2 for x in range(10)]
print(numbers2)

numbers3 = [x*x for x in range(10) if x%3 ==0]
print(numbers3)

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList1 = [letter for letter in myString]
print(myList1)

years = [1983, 1999, 1995, 1997, 1956, 1968]
ages = [2023-year for year in years]
print(ages)

results = [x if x%2==0 else 'Tek' for x in range(10)]
print(results)

result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

result1 = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(result1[0:9])
print(result1[9:18])
print(result1[18:27])