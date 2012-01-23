from millerrabin import is_probable_prime # .8s instead of 130s using is_prime

n = 1 # circle counter
total = 1 # 1 at the center belongs to all diagonal
prime = 0
while True:
    for i in (0, 2, 4, 6):
        # testing diagonal values for primality
        if is_probable_prime( (2 * n + 1) ** 2 - i * n ):
            prime += 1
        total += 1
    # testing ratio
    if prime * 100 / total < 10:
        # the side lenght is ...
        print 2 * n + 1
        break
    # next circle
    n += 1
