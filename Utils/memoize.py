class Memoize:
    """Memoize it's a decorator that will optimze the call of every function
    but also reduce the amount of time of process if the value has already been 
    previously calulcated, returning it directl.

    Returns:
        function: a function decorated
    """    
    def __init__(self, func):
      
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]
