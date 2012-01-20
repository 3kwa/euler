from operator import mul

def fac(n):
    """
    >>> fac(0)
    1
    >>> fac(1)
    1
    >>> fac(5)
    120
    """
    return reduce(mul, range(1, n + 1)) if n > 0 else 1

def choose(r, n):
    """
    >>> choose(10, 23)
    1144066L
    """
    return fac(n) / ( fac(r) * fac(n - r) )

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    result = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if choose(r, n) > 1000000:
                result += 1
    print result
