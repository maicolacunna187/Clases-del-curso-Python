"""
Funciones Lambda en Python: Sintaxis y Aplicaciones Prácticas

"""

# Función sencilla

def increment(x):
    return x + 1

resultado_v1 = increment(10)
print(resultado_v1)

# Función Labda

incremetn_v2 = lambda x : x + 1

resultado_v2 = incremetn_v2(20)
print(resultado_v2)

# Función Labda 2

full_name = lambda name, last_name: f"Full name is {name.title()} {last_name.title()}"

text = full_name("maicol", "acuña")
print(text)