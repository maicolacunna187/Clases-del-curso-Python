"""
Uso de la función map en Python para transformar listas

"""

numbers = [1, 2, 3, 4, 5]
number_v2 = []

# Función sin map y lambda

for i in numbers:
    number_v2.append(i * 2)

print(numbers)
print(number_v2)

# Función con map y lambda

number_v3 = list(map(lambda i: i * 2, numbers))
print(number_v3)

# Iterar y modificar dos listas

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)
