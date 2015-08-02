import time

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# This problem simply borrows and applies what was achieved in Problem7.py, the sieve of Eratosthenes

def get_primes_below(n):
    values = [True] * (n + 1)  # creates an array with n + 1 True elements

    # Set indices 0 and 1 to False, as 0 and 1 aren't prime numbers
    values[0] = False
    values[1] = False

    # Get the only even prime out of the way
    i = 2
    j = i
    # i <= n / i because because j will be multiplying by i to turn the appropriate array index False.
    # This means i * j cannot exceed n / i, or else it goes out bounds of the array's indices.
    # e.g. for n == 11, i = 2, j = i, I can access values[i * j], [i * j+1], [i * j+2], [i * j+3] and none higher
    # because [i * j+3] == values[2 * 5] == values[10], and j had to be less/equal than the limit n / i, which is
    # 11 / 2 == 5.
    while j <= n / i:
        values[i * j] = False
        j += 1

    # Now all primes henceforth are odd, so I can use i += 2
    i = 3
    while i <= n / i:
        if values[i]:
            j = i
            while j <= n / i:
                values[i * j] = False
                j += 1
        i += 2

    return values

def sum_primes(values):
    sum = 0
    i = 0
    while i < len(values):
        if values[i]:
            sum += i
        i+= 1

    return sum

print sum_primes(get_primes_below(2000000))  # 142913828922
