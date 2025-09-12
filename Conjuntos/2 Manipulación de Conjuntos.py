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

"""
Resumen ⚡🐍

Conjuntos 🧩: 
    colecciones desordenadas sin duplicados.

Agregar elementos ➕:

    set_countries = {'Colombia', 'Mexico', 'Chile'}
    set_countries.add('Perú')  # añade un solo elemento


Agregar varios elementos 🔄:

    nuevos_paises = {'Argentina', 'Ecuador', 'Perú'}
    set_countries.update(nuevos_paises)  # añade varios sin duplicar


Eliminar elementos ➖:

    set_countries.remove('Colombia')  # lanza error si no existe
    set_countries.discard('ARG')      # no lanza error si no existe


Vaciar conjunto 🧹:

    set_countries.clear()
    print(set_countries)  # set()


Ventaja 💡: control total sobre colecciones, con métodos seguros y 
            eficientes para añadir, actualizar y eliminar elementos.

"""