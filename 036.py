def is_palindrome(string):
    """
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('a')
    True
    """
    return string == string[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum(i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]))
