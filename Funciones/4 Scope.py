"""
Entendiendo el Scope en Python: Variables y Funciones

"""

price = 100 # global
result = 200 

def increment():
    price = 200 # local
    resultado = price + 10
    print(price)
    return resultado

print(price)

price_2 = increment()
print(price_2)
print(result)