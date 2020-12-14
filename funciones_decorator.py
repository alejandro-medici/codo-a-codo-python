import math

def succ(x):
    return x + 1
successor = succ
successor(10)

del succ
successor(10)

def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" 
    return result

print(temperature(20))



def factorial(n):
    """ calculates the factorial of n, 
        n should be an integer and n <= 0 """
    def inner_factorial(n):
        if n == 0:
            return 1
        else:
            return n * inner_factorial(n-1)
    if type(n) == int and n >=0:
        return inner_factorial(n)
    else:
        raise TypeError("n should be a positve int or 0")




def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))   

def polynomial_creator(*coefficients):
    """ coefficients are in the form a_n, ... a_1, a_0 
    """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients[::-1]):
            res += coeff * x** index
        return res
    return polynomial
  
p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(1, 8, -1, 3, 2)
p4  = polynomial_creator(-1, 2, 1)


for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo2(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo2("Hi")
    
print("We now decorate foo with f:")
foo2 = our_decorator(foo2)

print("We call foo after decoration:")
foo2(42)


@our_decorator
def foo3(x):
    print("Hi, foo has been called with " + str(x))

foo3("Hi")