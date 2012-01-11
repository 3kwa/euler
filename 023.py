from math import sqrt

def divisors(number):
    """
    >>> divisors(4)
    [1, 2]
    >>> divisors(28)
    [1, 2, 4, 7, 14]
    """
    return [d for d in range(1,number) if number % d == 0]

def d(number):
    """
    >>> d(220)
    284

    28 is a perfect number
    >>> d(28)
    28
    """
    # takes 55 seconds
    # return sum(d for d in divisors(number))

    # takes 0.5 seconds
    result = 1
    for i in range(2, int(sqrt(number)) + 1):
        if (number % i == 0):
            result += i
            if i != number/i:
                result += number / i
    return result

def is_abundant(number):
    """
    >>> is_abundant(12)
    True
    >>> is_abundant(11)
    False
    """
    return d(number) > number

# 28123 is upper limit
ABUNDANTS = set(number for number in range(28123) if is_abundant(number))

def is_sum_of_abundants(number):
    """
    >>> is_sum_of_abundants(24)
    True
    >>> is_sum_of_abundants(23)
    False
    """
    for i in (abundant for abundant in ABUNDANTS if abundant <= number / 2):
        if number - i in ABUNDANTS:
            return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

    total = 0
    for number in range(28123):
        total += 0 if is_sum_of_abundants(number) else number

    print sum(number for number in range(28123) if not is_sum_of_abundants(number))

