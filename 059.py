from itertools import cycle
from itertools import permutations


# cipher from cipher1.txt
with open('cipher1.txt') as f:
    cipher = map(int, f.read().replace('\r\n','').split(','))

lowercase = range(ord('a'), ord('z') + 1)
uppercase = range(ord('A'), ord('Z') + 1)

# we know the key contains lowercase only
for i in lowercase:
    # applying a single character key to the cipher
    xored = ''.join(chr(c ^ i) for c in cipher)
    # counting the number of spaces in the final text and alphanumerical
    print chr(i), xored.count(' '), sum(1 for c in xored if ord(c) in lowercase + uppercase)

# c, d, e, g and o are the most likely candidates (really it is d, g and o but
# we can make it more interesting with 5 candidates ;)

# we know the key to be 3 characters long
for key in set(p[:3] for p in permutations('cdego')):
    # display the key and the first 100 character of deciphered text
    print key, ''.join(chr(c ^ ord(k)) for c, k in zip(cipher[:100], cycle(key)))


# god is the key!
print sum(c ^ ord(k) for c, k in zip(cipher, cycle('god')))
