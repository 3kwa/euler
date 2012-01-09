def is_palindrome(number):
    """
    >>> is_palindrome(9009)
    True
    >>> is_palindrome(123)
    False
    >>> is_palindrome(98089)
    True
    """
    string = str(number)
    count = len(string) / 2
    return string[:count] == string[-count:][::-1]

def palindromic_product():
    for i in range(100,1000):
        for j in range(100, 1000):
             product = i * j
             if is_palindrome(product):
                 yield product


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
    print max(p for p in palindromic_product())
