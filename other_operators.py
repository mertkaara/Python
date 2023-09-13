# Identity operator: is
# Değişkenin değerlerinin aynı olup olmadığını değil de RAM adreslerinin aynı olup olmadığını inceler

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y)
print(x == z)
print(x is z) # False gelir çünkü ram adresleri farklı

# Membership operator: in
x =['apple','banana']
print('banana' in x)

name = 'Mert'
print('e' in name)