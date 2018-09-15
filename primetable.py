import numpy as np
from tabulate import tabulate

from primes import get_primes_up_to_nth_smart

if __name__ == "__main__":
    primes = get_primes_up_to_nth_smart(10)
    size = len(primes)
    rows = np.zeros((size, size))
    for i in range(size): # This loop avoids calculating twice the same value (the table is symmetrical )
        for j in range(i, size):
            p = primes[i] * primes[j]
            rows[i, j] = p
            rows[j, i] = p
    rows = np.c_[primes, rows]
    print(tabulate(rows, headers=[''] + primes, tablefmt='grid'))
