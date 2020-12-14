def contador_de_llamadas(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper

#@contador_de_llamadas # -> factorial_2 =  contador_de_llamadas(factorial_2)
