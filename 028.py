"""
A little observation : the values of the half traversal going up to the right
from the center follow the sequence (2*n + 1)**2 where n is the distance
from the center: (1), 9, 25, 49

The other 3 diagonal going anti-clockwise follow the sequence
(2*n + 1)**2 - d*2*n  with d = 1, 2, 3
"""

def function(d):
    """
    >>> d1 = function(0)
    >>> d1(1)
    9
    >>> d1(2)
    25
    >>> d1(3)
    49
    >>> d2 = function(1)
    >>> d2(1)
    7
    """
    return lambda n: (2*n + 1)**2 - d*2*n

def sum_diag(size):
    """
    >>> sum_diag(5)
    101
    """
    result = 1 # the center counted only once
    for d in range(4):
        for i in range(1, size/2 + 1):
            f = function(d)
            result += f(i)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum_diag(1001)
