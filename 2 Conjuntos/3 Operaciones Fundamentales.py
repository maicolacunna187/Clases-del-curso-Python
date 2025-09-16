"""
Operaciones Fundamentales con Conjuntos en Python

"""

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Unión

set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# Intersección

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# Diferencia

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# Diferencia simetrica

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)

