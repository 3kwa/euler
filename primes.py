def generator(stop=None):
    """
    http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
    http://stackoverflow.com/questions/567222/simple-prime-generator-in-python

    >>> list(generator(2))
    [2]
    >>> p = generator()
    >>> p.next()
    2
    >>> p.next()
    3
    """
    D = {}
    q = 2
    while (q <= stop if stop is not None else True):
        if q not in D:
            D[q * q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def factors(number):
    """
    >>> f = factors(4)
    >>> f.next()
    (2, 2)
    >>> list(factors(6))
    [(2, 1), (3, 1)]
    >>> list(factors(12))
    [(2, 2), (3, 1)]
    """
    for p in generator():
        if number < p / 2:
            break
        if number % p == 0:
            e = exponent(number, p)
            number = number / (p ** e)
            yield p, e

def exponent(number, prime):
    """
    >>> exponent(2, 2)
    1
    >>> exponent(8, 2)
    3
    >>> exponent(12, 2)
    2
    """
    e = 0
    while number % prime == 0:
        e += 1
        number = number / prime
    return e

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
