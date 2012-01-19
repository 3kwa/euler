from math import sqrt

from primes import generator

primes = list(generator(1000000))

def goldbach(number):
    """
    >>> goldbach(9)
    (7, 1)
    """
    for p in primes:
        if p > number:
            return None
        squared = sqrt( (number - p) / 2)
        if int(squared) == squared:
            return p, int(squared)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    number = 9
    while True:
        if goldbach(number) is None:
            print number
            break
        number += 2
