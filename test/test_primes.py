import pytest

import primes


def test_n_lessthan_1():
    with pytest.raises(AssertionError):
        primes.get_primes(1)
    with pytest.raises(AssertionError):
        primes.get_primes(0)
    with pytest.raises(AssertionError):
        primes.get_primes(-1)


PRIMES30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
PRIMES71 = PRIMES30 + [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

@pytest.mark.parametrize("max, expected", [
    (30, PRIMES30),
    (71, PRIMES71),
])
def test_getprimes(max, expected):
    assert expected == primes.get_primes(max)
