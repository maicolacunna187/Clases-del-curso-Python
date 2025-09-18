"""
Control manual de iteradores en Python con next

"""

# Forma automática
for i in range(1,11):
    print(i)


# Forma manual
my_iter = iter(range(1, 4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
