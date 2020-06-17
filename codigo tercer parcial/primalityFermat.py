import random

from scipy._lib.six import xrange


def fermat_test(n, k):
    # Implementation uses the Fermat Primality Test

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in xrange(k):
        a = random.randint(1, n - 1)

        if pow(a, n - 1) % n != 1:
            return False
    return True
n=11
k=3
if (fermat_test(n,k)):
    print(n,"es primo")
else:
    print(n,"no es primo")