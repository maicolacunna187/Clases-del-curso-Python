"""
Dictionary Comprehension con Condicionales en Python

"""
import random

countries = ['col', 'mex', 'bol', 'pe']


population_v2 = {country: random.randint(1,1000)                        
for country in countries}

print(population_v2)

result = {country: population
for (country, population) in population_v2.items() if population > 200}

print(result)

text = 'Hola, soy Maicol'
unique = {c: c for c in text if c in 'aeiou'}
print(unique)

