# distutils: language=c++

from libcpp.vector cimport vector
from libcpp.pair cimport pair

cdef extern from "prime_lib.hxx":
    cdef vector[pair[size_t, size_t]] prime_factors_impl(size_t)
    cdef vector[size_t] eratosthenes_impl(size_t)

def prime_factors(size_t n):
    return prime_factors_impl(n)

def eratosthenes(size_t n):
    return eratosthenes_impl(n)
