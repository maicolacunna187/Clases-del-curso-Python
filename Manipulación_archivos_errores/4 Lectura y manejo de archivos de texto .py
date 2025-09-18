"""
Lectura y manejo de archivos de texto en Python

"""
file = open("./text.txt")

# Leer archivos completos:
#print(file.read())

# Leer linea por linea:

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for i in file:
    print(i)

file.close()

# Esta instrucción cierra el close automáticamente

with open("./text.txt") as file:
    for line in file:
        print(line)