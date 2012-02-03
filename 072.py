from operator import mul
from fractions import Fraction

from primes import generator
from millerrabin import is_probable_prime


def factors(number, result=[]):
    """
    >>> factors(3)
    [3]
    >>> factors(4)
    [2]
    >>> factors(6)
    [2, 3]
    >>> factors(12)
    [2, 3]
    """
    if number == 1:
        return result
    if is_probable_prime(number):
        return result + [number]
    for p in generator():
        if number % p == 0:
            while number % p == 0:
                number = number / p
            return factors(number, result +[p])

def totient(n):
    """
    >>> totient(20)
    8
    >>> totient(97)
    96
    >>> totient(56)
    24
    """
    if is_probable_prime(n):
        return n - 1
    f = factors(n)
    return int( n * reduce(mul, ( (p-1) for p in f )) / reduce(mul, f)  )

def count(D):
    """
    >>> count(8)
    21
    """
    return sum(totient(n) for n in range(2, D + 1))


import doctest
doctest.testmod()

print count(1000000)
