import math
from funciones_1 import f
from Utils.contador_de_llamadas_definition import contador_de_llamadas
# import Utils.contador_de_llamadas_definition
from clase_objetos_1 import Persona
from factorial_decorator import factorial
from Utils.memoize import Memoize

@contador_de_llamadas
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

@Memoize
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    print("Este el entry point de mi programa")

    funcion_1 = f(1)
    funcion_2 = f(2)

    print(funcion_1(1))
    print(funcion_2(1))

    print (factorial_2.calls)
    for n in range(1, 10):
        print(n)
        print(factorial_2(n))
    print (factorial_2.calls)

    una_persona = Persona('ale')
    otra_persona = Persona('Francisco')
    print(una_persona)
    print(otra_persona)

    print(Persona.funcname)

    for n in range(1, 10):
        print(n)
        print(factorial(n))

    #Executed twice, please check the debug
    print(fibonacci(40))
    print(fibonacci(40))
    
main()
