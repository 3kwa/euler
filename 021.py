from collections import defaultdict

def divisors(number):
    """
    >>> divisors(4)
    [1, 2]
    """
    return [d for d in range(1,number) if number % d == 0]

def d(number):
    """
    >>> d(220)
    284
    """
    return sum(d for d in divisors(number))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

    all_ = []
    total = 0
    for number in range(10000):
        a, b = number, d(number)
        if (b, a) in all_:
            total += a + b
            all_.remove( (b, a) )
        else:
            all_.append( (a, b) )
    print total
