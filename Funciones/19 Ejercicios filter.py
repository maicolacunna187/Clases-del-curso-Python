"""
1. Números negativos
Tienes la lista numeros = [10, -3, 0, -7, 5, -1].
Usa filter y lambda para crear una nueva lista que contenga 
solo los números negativos.

"""

numeros = [10, -3, 0, -7, -5, -1]

numeros_negativos = list(filter(lambda x: x < 0, numeros ))
print(f"Números impares: {numeros_negativos}")

"""
2. Palabras que empiezan con vocal
Tienes la lista palabras = ["avion", "casa", "elefante", "sol", "iglesia"].
Usa filter y lambda para obtener solo las palabras que comiencen con una vocal.

"""

palabras = ["avion", "casa", "elefante", "sol", "iglesia"]

palabras_vocal = list(filter(lambda x: x[0] in ("a", "e", "i", "o", "u"), palabras))
print(f"Palabras que comienzan con una vocal: {palabras_vocal}")

"""
3. Filtrar valores altos
Tienes el diccionario notas = {"matematicas": 70, "historia": 55, "ingles": 80, "quimica": 45}.

Usa filter y lambda para obtener solo las asignaturas con nota mayor a 60.
"""
notas = {"matematicas": 70, "historia": 55, "ingles": 80, "quimica": 45}

notas_aprobadas = list(filter(lambda x: x[1] >= 60, notas.items()))
print(f"Asignaturas con nota mayor a 60: {notas_aprobadas}")

"""
4. Filtrar claves con cierta letra
Tienes el diccionario productos = {"pan": 1200, "leche": 3000, "queso": 8000, "arroz": 2500}.
Usa filter y lambda para obtener solo los productos cuyo nombre contenga la letra "e".

"""

productos = {"pan": 1200, "leche": 3000, "queso": 8000, "arroz": 2500}

productos_con_e = list(filter(lambda x: "e" in x[0], productos.items()))
print(f"Productos con nombre contenta la letra 'e': {productos_con_e} ")

