# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Typical elapsed times for each method to calculate the 10001st prime number on my laptop
# get_nth_prime_1: 0.7-0.9 seconds
# get_nth_prime_2: 0.1-0.3 seconds
# get_nth_prime_3: 0.4-0.6 seconds

# Brute-force

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    n_sqrt = n ** 0.5

    i = 3

    while i <= n_sqrt:
        if n % i == 0:
            return False
        i += 2

    return True

def get_nth_prime_1(n):
    if n == 1:
        return 2

    nth_prime = 0
    i = 3
    count = 1  # start at 1 since the first prime is already covered by the above 'if' condition

    while count < n:
        if is_prime(i):
            nth_prime = i
            count += 1
        i += 2

    return nth_prime

print get_nth_prime_1(10001)  # 104743

# More efficient solution using the sieve of Eratosthenes. The only problem is that the sieve captures
# all primes under a specific value, not the nth prime number. That means I have to provide an arbitrarily large
# number as the parameter for get_primes_until(n) and hope that the nth prime number will occur within that range.
# I've put in the magic number 120000 since I know from the brute-force approach that the 10001st prime is
# 104743. This alternate approach is dubious in this respect, despite being much faster.

def get_primes_below(n):
    values = [True] * (n + 1)  # creates an array with n + 1 True elements

    # Set indices 0 and 1 to False, as 0 and 1 aren't prime numbers
    values[0] = False
    values[1] = False

    # Get the only even prime out of the way
    i = 2
    j = i
    # j <= n / i because because j will be multiplying by i to turn the appropriate array index False.
    # This means i * j cannot exceed n / i, or else it goes out bounds of the array's indices.
    # e.g. for n == 11, i = 2, j = i, I can access values[i * j], [i * j+1], [i * j+2], [i * j+3] and none higher
    # because [i * j+3] == values[2 * 5] == values[10], and j had to be less/equal than the limit n / i, which is
    # 11 / 2 == 5.
    while j <= n / i:
        values[i * j] = False
        j += 1

    # Now all numbers henceforth are odd, so I can use i += 2
    i = 3
    while i <= n / i:
        if values[i]:
            j = i
            while j <= n / i:
                values[i * j] = False
                j += 1
        i += 2

    return values

def get_nth_prime_2(n):
    counter = 0
    values = get_primes_below(120000)  # how can I make this 1200000 constant more flexible for all other 'n' values?
    for i in range(2, len(values)):
        if values[i]:
            counter += 1
        if counter == n:
            return i

print get_nth_prime_2(10001)

# This approach avoids the use of an arbitrary array size for the sieve, but is less efficient because it must store
# each successive prime value until n inside an array. It is quicker, however, than the first approach.
#
# get_nth_prime_3() inserts the first prime number, 2, into an array that will be populated with n prime numbers
# I can avoid an is_prime() method to check whether each value is a prime number because I am dividing only with numbers
# already within the primes array. If any number has a remainder of 0 after being divided by a prime in the primes
# array, then that number cannot be prime.

def get_nth_prime_3(n):
    primes = [2]
    num_primes_found = 1
    potential_prime = 3

    while num_primes_found < n:
        i = 0
        prime_found = True
        potential_prime_sqrt = potential_prime ** 0.5
        # Originally the while condition below was "while i < len(primes)" which worked but was quite slow.
        # It checked whether the potential_prime was evenly divisible by every element in the primes array.
        #
        # This new condition only checks whether the actual element at index 'i' is less/equals than the square
        # root of the potential prime. Why does this still work? The same reason I used n_sqrt in my is_prime()
        # function; a number 'n' is composed of two natural numbered factors a * b, and one of either 'a' or 'b' must be
        # less/equal than sqrt(n), and the other greater than sqrt(n). That less/equal factor will never exceed
        # sqrt(n). E.g. sqrt(12) = 3.46. factors of 12 = 1 * 12, 2 * 6, and 3 * 4. The lesser factors
        # never exceed 3.46. E.g. sqrt(16) = 4. factors of 16 = 1 * 16, 2 * 8, 4 * 4. The lesser factors never exceed
        # 4.
        # Therefore if my divisor, primes[i], exceeded sqrt(potential_prime_sqrt), then I'd be past my bounds of
        # interest; I'd be testing numbers that exceed the sqrt(n) and thus will never be the "lesser factor" of n.
        #
        # In other words:  if n = a * b and a <= b then a * a <= a * b = n
        while primes[i] <= potential_prime_sqrt:
            if potential_prime % primes[i] == 0:
                prime_found = False
                break
            i += 1

        if prime_found:
            primes.append(potential_prime)
            num_primes_found += 1
        potential_prime += 2  # all potential primes from 3 onwards will be odd, so I can += 2

    return primes[len(primes) - 1]

print get_nth_prime_3(10001)
