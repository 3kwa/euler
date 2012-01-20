from collections import Counter

from primes import generator, is_prime

def first_member(D, SIZE):
    """
    Returns the first member of a family of SIZE primes obtain by substituting
    the same digit D times (0 to 9)

    >>> first_member(1, 6)
    13
    >>> first_member(2, 7)
    56003
    """

    for p in generator(1000000):
        string = str(p)
        counter = Counter(string)
        if D in counter.values():
            # getting the digit
            for digit, count in counter.iteritems():
                if count == D:
                    break
            # building the family
            family = []
            for d in range(10):
                # substitute digits
                member = string.replace(str(digit), str(d))

                # skipping if start with 0
                if member[0] == '0':
                    continue

                # testing for primality
                member = int(member)
                if is_prime(member):
                    family.append(member)

            if len(family) == SIZE:
                return p


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print first_member(3, 8)
