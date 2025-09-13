"""
Manipulación de Conjuntos: Agregar, Remover y Actualizar Elementos

"""

set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('arg' in set_countries)

# add
set_countries.add('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

# update
set_countries.update({'pe', 'ecua', 'arg'})
print(set_countries)

# remove

set_countries.remove('col')
print(set_countries)

set_countries.remove('arg')
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

set_countries.clear()
print(len(set_countries))

