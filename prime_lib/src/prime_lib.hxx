#include <vector>
#include <utility>
#include <cmath>
#include <iostream>

typedef std::pair<size_t, size_t> Pair;

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

void div(std::vector<Pair> & factors, size_t & n, size_t const & i)
{
    if (n % i == 0)
    {
        factors.push_back(Pair(i, 1));
        n /= i;
    }
    while (n % i == 0)
    {
        ++factors.back().second;
        n /= i;
    }
}

std::vector<Pair> prime_factors_impl(size_t n)
{
    std::vector<Pair> factors;
    div(factors, n, 2);
    
    for (size_t i = 3; i <= n; i += 2)
    {
        if (i*i > n)
        {
            factors.push_back(Pair(n, 1));
            break;
        }
        div(factors, n, i);
        if (n == 1)
        {
            break;
        }
    }
    
    if (factors.empty())
    {
        factors.push_back(Pair(1, 1));
    }
    
    return factors;
}

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

