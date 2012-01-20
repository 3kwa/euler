from itertools import permutations
from collections import defaultdict

from primes import generator

four_digits_prime = [p for p in generator(10000) if p>999]

candidates = defaultdict(list)

for prime in four_digits_prime:

    # generating a set of all the permutations of the digit of prime
    permutations_of_prime = set(map(
        lambda tuple_:int(''.join(tuple_)),
        permutations(str(prime))))

    # for every permutation
    for permutation in permutations_of_prime:
        # check for primality, 3330 and greater than prime (key is smallest prime)
        if permutation in four_digits_prime and \
           (permutation - prime) % 3330 == 0 and \
           permutation > prime:
            candidates[prime].append(permutation)

# display the concatenated string of 3 primes satisfying the conditions
for k,v in candidates.iteritems():
    v.append(k)
    if len(v) == 3:
        print ''.join(map(str,sorted(v)))

