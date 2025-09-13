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

"""
Resumen ⚡🐍

Conjuntos 🧩 :
    permiten operaciones útiles en programación, matemáticas 
    y ciencia de datos.

Unión ➕ 
    (todos los elementos sin duplicados):

        conjunto_A | conjunto_B
        # o conjunto_A.union(conjunto_B)


Intersección 🔗 
    (elementos comunes):

        conjunto_A & conjunto_B
        # o conjunto_A.intersection(conjunto_B)


Diferencia ➖ 
    (elementos de A que no están en B):

        conjunto_A - conjunto_B
        # o conjunto_A.difference(conjunto_B)


Diferencia simétrica 🔄 
    (todo menos los comunes):

        conjunto_A ^ conjunto_B
    # o conjunto_A.symmetric_difference(conjunto_B)


Ventaja 💡: permiten combinar, comparar y filtrar datos de forma rápida 
y eficiente.
"""