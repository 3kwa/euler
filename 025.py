def fibonacciGenerator():
    """
    >>> fib = fibonacciGenerator()
    >>> [fib.next() for i in range(12)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    prev, last = 1 , 0
    while True:
        if last == 0:
            fib = 1
        else:
            fib = prev + last
        prev, last = last, fib
        yield fib


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    fib = fibonacciGenerator()
    n = 1
    while len(str(fib.next())) < 1000:
        n += 1
    print n

    # yes using Binet's formula and figuring out the solution by hand is elegant
    # phi = (1 + sqrt(5))/2
    # fn = ( phi ** n - (-phi) ** (-n) ) / sqrt(5)

