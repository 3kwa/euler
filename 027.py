from primes import is_prime, generator

def length_prime_sequence(function):
    """
    >>> length_prime_sequence( quadratic(0, 0) )
    0
    >>> length_prime_sequence( quadratic(1, 41) )
    40
    >>> length_prime_sequence( quadratic(-79, 1601) )
    80
    """
    i = 0
    while is_prime( function(i) ):
        i += 1
    return i

def quadratic(a, b):
    return lambda n : n*n + a*n + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    a, b = max(
        ( (a, b) for a in range(-999, 1000) for b in range(-999, 1000) ),
        key = lambda t: length_prime_sequence( quadratic(t[0], t[1]) )
        )
    print a * b
