def divisors(number):
    """
    >>> divisors(4)
    [1, 2]
    """
    return [d for d in range(1,number) if number % d]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
