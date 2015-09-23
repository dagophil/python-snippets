import sys
from prime_lib import prime_factors, eratosthenes


def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 60
    factors = [str(p) + "^" + str(e) for p, e in prime_factors(n)]
    print n, "=", " * ".join(factors)

    print "primes < 100 are", eratosthenes(100)


if __name__ == "__main__":
    main()
    sys.exit(0)

