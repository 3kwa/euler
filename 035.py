"""
A circular prime number can only contain the digits 1 3 7 and 9 but for 5

Every digit will be the end digit of a rotation hence can't be even 0, 2, 4, 6

Not can it be 5 (dividable by 5)

I went brute force :P
"""

from primes import generator, is_prime

def rotation(number):
    """
    >>> rotation(2)
    [2]
    >>> rotation(21)
    [21, 12]
    >>> rotation(197)
    [197, 971, 719]
    """
    result = []
    string = str(number)
    for i in range(len(string)):
        result.append( int(string[i:] + string[:i]) )
    return result

def is_circular_prime(number):
    """
    >>> is_circular_prime(197)
    True
    >>> is_circular_prime(8)
    False

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97

    >>> [number for number in generator(100) if is_circular_prime(number)]
    [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
    >>> sum(1 for number in generator(100) if is_circular_prime(number))
    13
    """
    if number not in (2, 5):
        if '5' in str(number):
            return False
        for digit in str(number):
            if int(digit) % 2 == 0:
                return False
    # the previous 6 lines make the execution time go from 65 sec to 3 sec
    return all(is_prime(i) for i in rotation(number))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum(1 for number in generator(1000000) if is_circular_prime(number))
