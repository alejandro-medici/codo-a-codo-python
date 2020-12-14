from Utils.checkers import *

@factorial_decorator
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
