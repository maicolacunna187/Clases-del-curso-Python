"""
1. Tienes una lista de números, multiplícalos por 2 usando map y lambda.

numeros = [1, 2, 3, 4, 5]

"""
numeros = [1, 2, 3, 4, 5]

new_numbers = list(map(lambda x: x * 2, numeros))

print(f"Resultado: {new_numbers}")

"""
Convierte una lista de palabras a mayúsculas usando map y lambda.

palabras = ["python", "juego", "logica", "funcion"]

"""
palabras = ["python", "juego", "logica", "funcion"]

new_words = list(map(lambda x: x.upper(), palabras))

print(f"Resultado: {new_words}")

"""
Suma 10 a todas las notas de un diccionario usando map y lambda.

notas = {
    "matematicas": 70,
    "historia": 55,
    "ingles": 80
}

"""
notas = {
    "matematicas": 70,
    "historia": 55,
    "ingles": 80
}

new_notes = list(map(lambda valor: valor + 10, notas.values()))
print(f"Resultado: {new_notes}")

"""
Convierte todas las claves de un diccionario a mayúsculas usando map y lambda.

productos = {
    "pan": 1200,
    "leche": 3000,
    "queso": 8000
}

"""
productos = {
    "pan": 1200,
    "leche": 3000,
    "queso": 8000
}
new_keys = list(map(lambda clave: clave.upper(), productos.keys()))
print(f"Resultado: {new_keys}")

"""
Tienes el siguiente diccionario con productos y sus precios:

productos = {
    "pan": 1200,
    "leche": 3000,
    "queso": 8000
}

Objetivo:

Aumentar el precio de cada producto en un 10% y crear un nuevo diccionario con los mismos nombres de productos pero con los precios actualizados.

Debes usar map y lambda para lograrlo.

"""
productos = {
    "pan": 1200,
    "leche": 3000,
    "queso": 8000
}

increase_price = map(lambda item: (item[0], item[1] * 1.1), productos.items())

productos_actualizados = dict(increase_price)

print(productos_actualizados)

modified_dictionary = map(lambda item: (item[0].upper(), item[1] * 1.1), productos.items())

new_dicctionary = dict(modified_dictionary)
print(new_dicctionary)