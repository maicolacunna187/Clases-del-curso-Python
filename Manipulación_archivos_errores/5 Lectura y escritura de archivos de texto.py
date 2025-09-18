"""
Lectura y escritura de archivos de texto en Python

"""

with open("./text.txt", "w+") as file:
    for line in file:
        print(line)

    file.write("nuevas cosas en este archivo\n")
    file.write("otra lina\n")
    file.write("mas lineas\n")

    