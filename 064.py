from math import sqrt


def step(value):
    return int(value), ( value + int(value) ) / (value ** 2 - int(value) ** 2)

def recursion(value, seen=[]):
    integer, new = step(value)
    # floating point precision an issue must truncate/round
    # 3 was chosen empirically 10 ** -4 precision in assessing periodicity
    truncated = round(new, 1)
    if truncated in seen:
        return len(seen)
    return recursion(new, seen + [truncated])

def period(N):
    """
    >>> [period(n) for n in (2, 3, 5, 6, 7, 8, 10, 11, 12, 13)]
    [1, 2, 1, 2, 4, 2, 1, 2, 2, 5]
    >>> period(23)
    4
    """
    value = sqrt(N)
    if int(value)==value:
        return 0
    return recursion(sqrt(N))

def solution(max):
    """
    >>> solution(13)
    4
    """
    return sum(1 for n in range(2, max + 1) if period(n) % 2 != 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

print solution(10000)
