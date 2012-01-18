"""
http://mathworld.wolfram.com/Factorion.html
"""

from operator import mul

def fac(n):
    """
    >>> fac(0)
    1
    >>> fac(1)
    1
    >>> fac(4)
    24
    """
    if n == 0:
        return 1
    return reduce(mul, range(1, n + 1))

def is_sum_of_fac_digit(n):
    """
    >>> is_sum_of_fac_digit(145)
    True
    >>> is_sum_of_fac_digit(1)
    False
    """
    if n in (1,2):
        return False
    return sum(fac(int(i)) for i in str(n)) == n

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum(n for n in range(100000) if is_sum_of_fac_digit(n))
