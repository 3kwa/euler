"""
n >= 2 and n can't be greater than 9 (we are looking for a 9 digit number)

if n = 2, number must be 9999 max because 2 * 9999 = 19998 which 5 + 4 digits
"""

def concatenated_product(number, n):
    """
    >>> concatenated_product(192, 3)
    192384576
    >>> concatenated_product(9, 5)
    918273645
    """
    return int(''.join(str(number * i) for i in range(1, n + 1)))

def is_pandigital(number, n):
    """
    >>> is_pandigital('13', 3)
    False
    >>> is_pandigital('132', 3)
    True
    """
    return sorted(str(number)) == [str(i) for i in range(1,n + 1)]

def pandigital_concatenated_product(number, n):
    """
    >>> pandigital_concatenated_product(192, 3)
    192384576
    >>> pandigital_concatenated_product(123, 2)
    0
    """
    product = concatenated_product(number, n)
    return product if is_pandigital(product, 9) else 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print max(  pandigital_concatenated_product(number, n)
                for number in range(1,10000)
                for n in range(1,10) )
