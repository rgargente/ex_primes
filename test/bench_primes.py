import pytest

import primes


@pytest.mark.parametrize("n, function", [
    (10, primes.get_primes_up_to_nth_simple),
    (10, primes.get_primes_up_to_nth_sieve),
    (100, primes.get_primes_up_to_nth_simple),
    (100, primes.get_primes_up_to_nth_sieve),
    (500, primes.get_primes_up_to_nth_simple),
    (500, primes.get_primes_up_to_nth_sieve),
    (1000, primes.get_primes_up_to_nth_simple),
    (1000, primes.get_primes_up_to_nth_sieve),
    (10000, primes.get_primes_up_to_nth_simple),
    (10000, primes.get_primes_up_to_nth_sieve),
])
def test_get_primes_up_to_nth(benchmark, n, function):
    benchmark(function, n)
