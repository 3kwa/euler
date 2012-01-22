def step(number):
    """
    >>> step(47)
    121
    """
    return number + int(str(number)[::-1])

def is_palindrome(number):
    """
    >>> is_palindrome(47)
    False
    >>> is_palindrome(121)
    True
    """
    return str(number) == str(number)[::-1]

def is_lychrel(number):
    """
    >>> is_lychrel(47)
    False
    >>> is_lychrel(349)
    False
    >>> is_lychrel(196)
    True
    >>> is_lychrel(10677)
    True
    """
    for i in range(50):
        number = step(number)
        if is_palindrome(number):
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum(1 for i in range(10000) if is_lychrel(i))
