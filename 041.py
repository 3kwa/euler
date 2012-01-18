"""
http://eli.thegreenplace.net/2006/07/11/sum-of-digits-and-divisibility-by-3/

1+2+3+4+5+6+7+8+9 = 45 (never prime, multiply of 3)
1+2+3+4+5+6+7+8   = 36 (never prime, multiply of 3)
1+2+3+4+5+6+7     = 28
1+2+3+4+5+6       = 21 (never prime, multiply of 3)
1+2+3+4+5         = 15 (never prime, multiply of 3)
1+2+3+4           = 10
1+2+3             = 6 (never prime, multiply of 3)
1+2               = 3 (never prime, multiply of 3)
"""

from primes import is_prime

def recursive(size=9, selected=[]):
    """
    recursive generator of (n=size)-digits pandigital numbers in descending order
    """
    if len(selected) == size:
        yield int( ''.join(map(str, selected)) )
    for i in range(size, 0, -1):
        if i not in selected:
            for result in recursive(size, selected + [i]):
                yield result

def first_prime(generator):
    """
    given a generator return the first prime it encounters
    """
    try:
        number = generator.next()
        while not is_prime(number):
            number = generator.next()
    except StopIteration:
        return None
    else:
        return number

for n in (7, 4):
    result = first_prime(recursive(n))
    if result is not None:
        print result
        break
