import math

# 3! = 3 * 2 * 1
# 25! = 25 * (n-1) * 1
# n! = n * (n-1) * (n-2) ... * 1
def factorial(x):
    if type(x) == int and x >= 0:
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    else:
        raise TypeError("Error, no se puede realizar operacion")


mi_resultado = factorial(3)

print(mi_resultado)

for n in range(1, 10):
    print(n)
    print(factorial(n))

#print(factorial(1-2))

#print(factorial('Hola'))

# Otro tipo factorial
def factorial_2(x):

    def factorial_interior(x):
        if x == 0:
            return 1
        else:
            return x * factorial_interior(x - 1)

    if type(x) == int and x >= 0:
        return factorial_interior(x)
    else:
        raise TypeError("Error, no se puede realizar operacion")


for n in range(1, 10):
    print(n)
    print(factorial_2(n))

#print(factorial_2('Hola'))

def g():
    print("Esto es la funcion g")

def f(func):
    print("Estoy es la funcion f")
    func()
    print("Llamo a la funcion " + func.__name__)

f(g)


