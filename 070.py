from math import sqrt
from primes import generator

def is_permutation(a, b):
    return ''.join(sorted(str(a))) == ''.join(sorted(str(b)))

N = 10000000
primes = list( generator(N / 2) )

ratio = N
result = 0

for small in primes[:len(primes) / 2]:
    if small > sqrt(N):
        break
    for big in primes[len(primes)/2::-1]:
        if big <= small:
            break
        n = small * big
        if n <= N:
            phi = (small - 1) * (big - 1)
            if is_permutation(n, phi):
                man = float(n) / phi
                result, ratio = (n, man) if man < ratio else (result, ratio)

print result
