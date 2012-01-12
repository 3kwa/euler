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

    print sum(i for i in range(300000) if is_sum_of_nth_power_of_digits(i, 5))
