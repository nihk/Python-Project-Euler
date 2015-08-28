# Euler discovered the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However,
# when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41
# is clearly divisible by 41.
#
# The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values
# n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
# n^2 + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n = 0.


# Quasi brute-force. The prime-sieve is quite efficient, but the means of getting the quadratic is slow as it
# iterates through every possible combination of variables a and b.
def get_primes_under(limit):
    primes = [True] * limit
    primes[0], primes[1] = [False] * 2

    i = 2
    j = i
    while i * j < limit:
        primes[i * j] = False
        j += 1

    i = 3
    while i * i < limit:
        j = i
        if primes[i]:
            while i * j < limit:
                primes[j * i] = False
                j += 1
        i += 2

    return primes

def get_best_quadratic_product(limit=1000):
    # Determining the size of the prime sieve is arbitrary. This problem's description makes a note
    # of a discovery of a maximum sequence length of 80. I presumed that this mentioning was indicative that
    # longer sequences than that were few and far between, especially since n^2 - 79n + 1601 goes beyond the bounds
    # of |1000| with its 'b' term. Therefore, even though within the bounds of |1000| the max sequence will
    # likely be < 80 (it is in fact 71 for this range), I put the maximum sequence length as 200 to be safe.
    max_sequence_length = 200
    primes_sieve_size = max_sequence_length ** 2 + limit * max_sequence_length + limit
    primes = get_primes_under(primes_sieve_size)
    largest_n = 0
    product = 0

    for a in range(-limit, limit + 1):
        for b in range(-limit, limit + 1):
            n = 0
            while primes[abs(n * n + a * n + b)]:
                n += 1

            if n > largest_n:
                largest_n = n
                product = a * b

    return product


print get_best_quadratic_product()  # -59231
