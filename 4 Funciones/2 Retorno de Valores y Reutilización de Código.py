"""
Funciones en Python: Retorno de Valores y Reutilización de Código

"""

def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min,max):
        sum += x
    return sum

result = sum_with_range(1, 11)
print(result)
result_2 = sum_with_range(result, result + 31)
print(result_2)
