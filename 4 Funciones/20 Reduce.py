"""
Uso de Reduce en Python para Manipular Listas

"""
import functools

numbers = [1, 2, 3, 4]

def acumm(counter, item):
    print(f"Counter: {counter}")
    print(f"Item: {item}")

    return counter + item

result = functools.reduce(lambda counter, item: counter + item, numbers)
result_v2 = functools.reduce(acumm, numbers)

print(result)
print(result_v2)

