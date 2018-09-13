import numpy as np
from tabulate import tabulate

from primes import get_primes_up_to_nth_smart

if __name__ == "__main__":
    primes = get_primes_up_to_nth_smart(10)
    size = len(primes)
    rows = np.tile(primes, (size, 1))
    for i, p in enumerate(primes):
        rows[i, :] *= p
    rows = np.c_[primes, rows]
    print(tabulate(rows, headers=[''] + primes, tablefmt='grid'))
