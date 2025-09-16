"""
List Comprehension en Python: Sintaxis y Ejemplos Prácticos

"""

"""
numbers = []
for element in range(1,11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)

"""
# Método 1

numbers = []
for element in range(1,101):
    if element % 2 == 0:
        numbers.append(element * 2)

print(numbers)

# Método 2

numbers_v2 = [element * 2 for element in range(1,101) if element % 2 == 0]
print(numbers_v2)

