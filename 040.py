from operator import mul

def digit(n):
    """
    Returns the nth digit of the irrational decimal created by
    the concatenation of positive integers from 1 onwards:

    0.12345678910111213141516171819202122...

    >>> digit(1)
    1
    >>> digit(10)
    1
    >>> digit(11)
    0
    >>> digit(12)
    1
    >>> digit(27)
    8
    """
    index = 0
    for i in range(1, n + 1):
        add = len(str(i))
        if index + add < n:
            index += add
        else:
            return int( str(i)[n-index-1] )

def generator():
    """
    Generator returning a tuple index, digit for the irrational decimal ...

    >>> g = generator()
    >>> g.next()
    (1, 1)
    >>> g.next()
    (2, 2)
    >>> [digit for index, digit in [g.next() for i in range(15)]]
    [3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3]

    We could compute the result using the generator and :

    g = generator()
    product = 1
    while  True:
        index, digit = g.next()
        if index in (1, 10, 100, 1000, 10000, 100000, 1000000):
            product *= digit
        if index == 1000000:
            break
    print product

    but it is much slower :P
    """
    index = 0
    integer = 1
    while True:
        for d in str(integer):
            index += 1
            yield index, int(d)
        integer += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print reduce(mul, (digit(i) for i in (1, 10, 100, 1000, 10000, 100000, 1000000)))
