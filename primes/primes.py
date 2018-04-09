"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    if count < 1:
        return []

    primes = [2]

    i = 1
    j = 3

    while i < count:
        if is_prime(j, primes):
            primes.append(j)
            i += 1
        j += 1

    return primes

def is_prime(num, primes):
    for item in primes:
        if num % item == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
