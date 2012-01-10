import sys
from operator import mul
import primes

def triangle_number_generator():
    """
    >>> tn = triangle_number_generator()
    >>> tn.next()
    1
    >>> tn.next()
    3
    >>> tn.next()
    6
    """
    i = 1
    number = 0
    while True:
        number += i
        i += 1
        yield number

def factors_count(number):
    """
    >>> factors_count(1)
    1
    >>> factors_count(3)
    2
    >>> factors_count(6)
    4
    >>> factors_count(28)
    6
    """
    if number == 1:
        return 1

    return reduce(mul, (exponent + 1 for prime, exponent in primes.factors(number)))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
    for tn in triangle_number_generator():
        if factors_count(tn) > 500:
            print tn
            break
