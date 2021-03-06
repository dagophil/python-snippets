#ifndef PRIME_LIB_HXX
#define PRIME_LIB_HXX

#include <iostream>
#include <cmath>
#include <vector>
#include <tuple>
#include <set>
#include <utility>
#include <limits>
#include <algorithm>

typedef std::pair<size_t, size_t> Pair;

/**
 * Compute the prime numbers in the interval [2, N] and return them.
 */
std::vector<size_t> eratosthenes_impl(size_t N)
{
	std::vector<bool> marked(N+1);
	marked[0] = true;
	marked[1] = true;
	for (size_t i = 2; i*i < marked.size(); ++i)
	{
		if (!marked[i])
		{
			for (size_t j = 2; i*j < marked.size(); ++j)
			{
				marked[i*j] = true;
			}
		}
	}

	std::vector<size_t> primes;
	for (size_t i = 0; i < marked.size(); ++i)
	{
		if (!marked[i])
		{
			primes.push_back(i);
		}
	}

	return primes;
}

namespace detail
{
    /**
     * Finds the largest exponent e such that n is divisible by i^e.
     * n will be divided by i^e. If e > 0 then (i, e) will be appended to factors.
     */
    void div(std::vector<Pair> & factors, size_t & n, size_t const i)
    {
        if (n % i == 0)
        {
            factors.emplace_back(i, 1);
            n /= i;
        }
        while (n % i == 0)
        {
            ++factors.back().second;
            n /= i;
        }
    }
}

/**
 * Compute the prime factors of n.
 * The output is a vector of pairs (p, e), where p is a prime that divides n
 * and e is the maximum exponent such that p^e divides n.
 */
std::vector<Pair> prime_factors_impl(size_t n)
{
    std::vector<Pair> factors;
    detail::div(factors, n, 2);
    
    for (size_t i = 3; i <= n; i += 2)
    {
        if (i*i > n)
        {
            factors.emplace_back(n, 1);
            break;
        }
        detail::div(factors, n, i);

        if (n == 1)
            break;
    }
    
    if (factors.empty())
        factors.emplace_back(1, 1);
    
    return factors;
}

/**
 * Returns true if n is prime, else false.
 */
bool is_prime_impl(size_t n)
{
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (size_t i = 5; i*i <= n; i+=6)
        if (n % i == 0 || n % (i+2) == 0)
            return false;
    return true;
}

/**
 * Return the greatest common divisor of a and b.
 */
template <typename T>
T gcd(T a, T b)
{
    return b == 0 ? a : gcd(b, a % b);
}

namespace detail
{
    /**
     * Compute the next value in the continued fraction of sqrt(d)
     * and update the current variables.
     */
    size_t next_cfr(long & b, long & c, size_t d)
    {
        size_t x = (c*std::sqrt(d) - b*c) / (d - b*b);
        long cc = d - b*b;
        long bb = -b*c - x*cc;

        auto g = gcd(c, gcd(bb, cc));
        if (g < 0)
            g = -g;
        if (cc < 0)
            g = -g;
        b = bb/g;
        c = cc/g;

        return x;
    }
}

/**
 * Returns a pair (f, p) where f is the continued fraction of sqrt(d) and
 * p is the period length. If p == 0 then the maximum number of iterations 
 * was reached before finding the period length.
 */
std::pair<std::vector<size_t>, size_t>
cfr_impl(size_t d, size_t max_iter = 2000)
{
    using namespace std;

    // The container for the continued fraction.
    vector<size_t> out;

    // Storage for the residuums to recognize periodicity.
    typedef tuple<long, long> tpl;
    set<tpl> s;

    // Initialization.
    long b = -floor(sqrt(d));
    long c = 1;
    s.emplace(b, c);
    out.push_back(-b);

    if ((size_t)b*b == d)
        throw runtime_error("cfr_impl(): d must not be a square.");

    // Iteratively compute the values of the continued fraction.
    for (size_t i = 0; i < max_iter; ++i)
    {
        // Compute next value in the continued fraction.
        auto x = detail::next_cfr(b, c, d);
        out.push_back(x);

        // Check for periodicity.
        auto p = s.emplace(b, c);
        if (!p.second)
            return make_pair(out, distance(p.first, s.end()));
    }

    return make_pair(out, 0);
}

namespace detail
{
    /**
     * Get the i-th value of the given continued fraction.
     */
    size_t eval_cfr(size_t i, std::vector<size_t> const & frac, size_t p)
    {
        if (i < frac.size())
            return frac[i];
        else if (p > 0)
            return frac[i - p * (size_t)std::ceil((double) (i+1-frac.size()) / p)];
        else
            throw std::runtime_error("eval_cfr(): Index out of range for non-periodic continued fraction.");
    } 
}

/**
 * Return (numerator, denominator) of the n-th approximation fraction of the given continued fraction.
 */
std::pair<size_t, size_t> approx_cfr_impl(size_t n, std::vector<size_t> const & frac, size_t p)
{
    using namespace std;

    // Initialization.
    size_t a = 1;
    auto b = detail::eval_cfr(n, frac, p);

    // Early out.
    if (n == 0)
        return make_pair(b, 1);

    // Loop over the continued fraction and compute numerator and denominator.
    for (size_t m = n-1; m > 0; --m)
    {
        auto new_b = detail::eval_cfr(m, frac, p)*b+a;
        a = b;
        b = new_b; 
    }
    a += b*detail::eval_cfr(0, frac, p);

    // Divide by the gcd.
    auto d = gcd(a, b);
    return make_pair(a/d, b/d);
}

#endif
