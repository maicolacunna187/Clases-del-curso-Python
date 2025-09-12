"""
Conjuntos en Python: Propiedades y Uso Práctico

"""

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)

"""
Resumen ⚡🐍

    Conjuntos (sets) 🧩: 
        estructura de datos para agrupar elementos únicos.

    Propiedades ✨:

        Modificables ➕➖

        Desordenados 🔀

        Sin duplicados ❌

Creación 🛠️:

    set_countries = {"Colombia", "México", "Bolivia"}
    print(set_countries)
    print(type(set_countries))


Tipos de datos variados 🎲: números, strings, booleanos.

    set_types = {1, "texto", False, 3.14}
    print(set_types)


Desde otras estructuras 🔄:

    String: set("hola") → {'h','o','l','a'}

    Tupla: set(("A","B","A")) → {'A','B'}

    Lista: elimina duplicados:

        numbers = [1,2,3,1]
        unique_set = set(numbers)
        unique_numbers = list(unique_set)


Ventajas 💡:

    Elimina duplicados automáticamente

    Operaciones de conjuntos: unión, intersección

    Búsqueda optimizada

"""