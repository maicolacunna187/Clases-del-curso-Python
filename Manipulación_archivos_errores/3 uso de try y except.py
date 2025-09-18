"""
Manejo de Errores en Python: Uso de Try y Except

"""
try:
    print( 7 / 0)
    assert 1 != 1, "Uno no es igual que uno"
    age = 10
    if age < 18:
        raise Exception("No se permiten menores de edad.")
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print("Hola")
print("Hola 2")