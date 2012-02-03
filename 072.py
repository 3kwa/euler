from operator import mul

from primes import generator
from millerrabin import is_probable_prime


# http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
   """Decorator that caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned, and
   not re-evaluated.
   """
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      """Return the function's docstring."""
      return self.func.__doc__
   def __get__(self, obj, objtype):
      """Support instance methods."""
      return functools.partial(self.__call__, obj)

@memoized
def factors(number):
    """
    >>> factors(3)
    [3]
    >>> factors(4)
    [2]
    >>> factors(6)
    [2, 3]
    >>> factors(12)
    [2, 3]
    """
    if is_probable_prime(number):
        return [number]
    for p in generator():
        if number % p == 0:
            while number % p == 0:
                number = number / p
            if number == 1:
                return [p]
            else:
                return [p] + factors(number)

def totient(n):
    """
    >>> totient(20)
    8
    >>> totient(97)
    96
    >>> totient(56)
    24
    """
    if is_probable_prime(n):
        return n - 1
    f = factors(n)
    # use (p - 1) / p instead of 1 - 1./p to avoid floating point error
    return n * reduce(mul, ( (p-1) for p in f )) / reduce(mul, f)

def count(D):
    """
    >>> count(8)
    21
    """
    return sum(totient(n) for n in range(2, D + 1))


import doctest
doctest.testmod()

print count(1000000)
