import sys
from prime_lib import prime_factors, eratosthenes, is_prime


def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 60
    factors = [str(p) + "^" + str(e) for p, e in prime_factors(n)]
    print n, "=", " * ".join(factors)

    primes = eratosthenes(100)
    print "primes < 100 are", primes
    
    for i in xrange(100):
        assert (i in primes and is_prime(i)) or (i not in primes and not is_prime(i))


if __name__ == "__main__":
    main()
    sys.exit(0)

