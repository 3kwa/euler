"""
if N has n digits N >= 10**n i.e. 1 followed by n-1 0

we are looking for N who are the sum of their digits so N < n*9**5

the smallest n for which 10**n > n*9**5 is 6

hence no integer above 6*9**5 = 354294 can be the sum of the fifth power of
its digits
"""

def is_sum_of_nth_power_of_digits(number, n):
    """
    >>> is_sum_of_nth_power_of_digits(1, 4)
    False
    >>> is_sum_of_nth_power_of_digits(1634, 4)
    True
    >>> is_sum_of_nth_power_of_digits(8208, 4)
    True
    >>> is_sum_of_nth_power_of_digits(9474, 4)
    True
    """
    if number < 2:
        return False
    return sum(int(d) ** n for d in str(number)) == number



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print sum(i for i in range(354294) if is_sum_of_nth_power_of_digits(i, 5))
