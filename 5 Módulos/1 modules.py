import sys
# sys → Proporciona acceso a variables y funciones relacionadas con el intérprete de Python.
# Aquí se usa sys.path para mostrar las rutas donde Python busca los módulos.

print(sys.path)


import re
# re → Permite trabajar con expresiones regulares para buscar y manipular texto.
# Aquí se usa re.findall para extraer todos los números de un texto.

text = "Mi número de telefono es: 321 485 6801, el codigo del pais es 57, mi numero de la suerte 3 "
result = re.findall('[0-9]+', text)
print(result)


import time
# time → Ofrece funciones para trabajar con fechas y horas.
# Se usa time.time para obtener el tiempo actual en segundos,
# time.localtime para convertirlo en formato legible
# y time.asctime para mostrarlo como cadena.

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)


import collections
# collections → Contiene estructuras de datos adicionales a las básicas de Python.
# Aquí se usa Counter para contar la frecuencia de cada número en una lista.

numbers = [1,1,2,1,2,1,4,5,3,3,1,21]
counter = collections.Counter(numbers)
print(counter)
