import random

"""
Comprensión de Diccionarios en Python: Ejemplos y Aplicaciones


"""

"""
dict = {}

for i in range(1,6):
    dict[i] = i * 2

print(dict)

dict_v2 = {i: i * 2 for i in range(1,6)}
print(dict_v2)

"""

"""
# Método 1

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1,1000)

print(population)

# Método 2

population_v2 = {country: random.randint(1,1000) for country in countries}

print(population_v2)

"""

names = ['nico', 'zule', 'santi']
ages = [12,56,68]

# Unir listas
print(list(zip(names, ages)))

# Dictionary Comprehension

new_dict = {name: age for (name, age) in list(zip(names, ages))}
print(new_dict)