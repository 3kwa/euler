from primes import generator, is_prime

def prime_sum_of_primes_generator(maximum):
    """
    >>> sop100 = prime_sum_of_primes_generator(100)
    >>> sop100.next()
    [2, 3]
    >>> max( (l for l in sop100), key=lambda l : len(l) )
    [2, 3, 5, 7, 11, 13]
    """
    primes = list( generator(maximum/2) )
    count = len(primes)
    sum_of_primes = []
    for start, prime in enumerate(primes):
        for stop in range(start + 1, count):
            consecutive = primes[start:stop]
            sum_ = sum(consecutive)
            if sum_ > maximum:
                break
            if is_prime(sum_) and len(consecutive) > 1:
                yield consecutive

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum( max(
        (l for l in prime_sum_of_primes_generator(1000000)),
        key=lambda l : len(l) ))
