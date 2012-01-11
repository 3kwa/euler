from operator import mul

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_reduce(n):
    # no recursion limit with reduce ... faster?
    return reduce(mul, xrange(1, n+1))

print sum(int(c) for c in str(factorial_reduce(100)))
