from itertools import permutations
from collections import defaultdict

from primes import generator

four_digits_prime = [p for p in generator(10000) if p>999]

candidates = defaultdict(list)

for prime in four_digits_prime:

    permutations_of_prime = map(
        lambda tuple_:int(''.join(tuple_)),
        permutations(str(prime)))
    permutations_of_prime.remove(prime)

    for permutation in permutations_of_prime:
        if permutation in four_digits_prime:
            candidates[prime].append(permutation)

def sequence_of_three(list_):
    differences = defaultdict(set)

    for index, value in enumerate(list_):
        for i in range(index + 1, len(list_)):
            other = list_[i]
            differences[abs(value-other)].update(set([value, other]))

    for k,v in differences.iteritems():
        if len(v) == 3 and k == 3330:
            return v

for k,v in candidates.iteritems():
    v.append(k)
    man = sequence_of_three(v)
    if man is not None:
        print man

