"""
13 5197 5701 6733 8389 - ugly but works :P
"""

from primes import generator
from millerrabin import is_probable_prime


P = list(generator(10000))

def valid(a, b):
    s1 = str(a)+str(b)
    s2 = str(b)+str(a)
    if is_probable_prime(int(s1)) and is_probable_prime(int(s2)):
        return True
    return False

found = False
for i in P:
    for j in (p for p in P if p > i):
        if not valid(i,j):
            continue
        for k in (p for p in P if p > j):
            if not valid(i,k) or not valid(j,k):
                continue
            for l in (p for p in P if p > k):
                if not valid(i,l) or not valid(j,l) or not valid(k,l):
                    continue
                for m in (p for p in P if p > l):
                    if not valid(i,m) or not valid(j,m) or not valid(k,m) or not valid(l,m):
                        continue
                    print i,j,k,l,m
                    found = True
                    break
                if found == True: break
            if found == True: break
        if found == True: break
    if found == True: break
