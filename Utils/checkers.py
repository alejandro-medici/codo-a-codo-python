def factorial_decorator(func):
    def checker(x):
        if type(x) == int and x >= 0:
            return func(x)
        else:
            raise TypeError("Error, no se puede realizar operacion")
    return checker
