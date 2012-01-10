def sequence(n):
    """
    >>> sequence(1).next()
    Traceback (most recent call last):
    StopIteration
    >>> list(sequence(13))
    [40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        yield n

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

    longest = 0
    number = 0
    for i in range(1, 1000000):
        length = len(list(sequence(i)))
        number, longest = (i, length) if length > longest else (number, longest)
    print number
