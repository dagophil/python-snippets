import sys
import math
from prime_lib import *


def main():
    # Check the prime factors of some numbers.
    assert prime_factors(7) == [(7, 1)]
    assert prime_factors(9) == [(3, 2)]
    assert prime_factors(60) == [(2, 2), (3, 1), (5, 1)]
    # factors = [str(p) + "^" + str(e) for p, e in prime_factors(n)]
    # print n, "=", " * ".join(factors)

    # Check the first 100 primes.
    primes = eratosthenes(100)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Check the continued fraction of square roots.
    assert cfr(2) == ([1, 2], 1)
    assert cfr(3) == ([1, 1, 2], 2)
    assert cfr(7) == ([2, 1, 1, 1, 4], 4)
    assert cfr(12) == ([3, 2, 6], 2)
    assert cfr(13) == ([3, 1, 1, 1, 1, 6], 5)

    # Check the approximation of the continued fraction of square roots.
    assert approx_cfr(3, d=2) == (17, 12)
    assert approx_cfr(3, cfrac=cfr(5)) == (161, 72)

    print "Success."


if __name__ == "__main__":
    main()
    sys.exit(0)
