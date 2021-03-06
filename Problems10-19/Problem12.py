# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

# Brute-force; this is tedious for large numbers like the one this problem wants me to find

def get_num_divisors(n):
    num_divisors = 0
    limit = n
    i = 1

    while i < limit:
        if n % i == 0:
            limit = n / i
            if limit != 1:  # Counts the complement divisor of i, but only if it's different from itself
                            # otherwise the factors of e.g. 4 would be counted like 1, 2, 2, 4 rather than
                            # 1, 2, 4
                num_divisors += 1
            num_divisors += 1
        i += 1

    return num_divisors

triangle_value = 0
num_divisors = 0
i = 1

while num_divisors <= 500:
    triangle_value += i
    num_divisors = get_num_divisors(triangle_value)
    i += 1

print triangle_value, "has", num_divisors, "divisors."  # 76576500 has 576 divisors

# A more efficient solution using the Tau function
# n = (p^a)(q^b)(r^c)...
# divisors(n) = (a + 1)(b + 1)(c + 1)...
# In other words: take for example the number 48. Start by dividing by the first prime, 2, until there is
# a remainder.
# 48 / 2 = 24.
# 24 / 2 = 12.
# 12 / 2 = 6.
# 6 / 2 = 3.
# 3 / 2 = 1.5, there is a remainder here so stop.
# 48 was able to be divided by 2 four times until a remainder is found; the number at this point is 3.
# 3 / 3 = 1
# 1 / 3 = 0.3~, there is a remainder here to stop. The number is also now 1, so don't test any more primes.
#
# 2 was divisible 4 times, 3 one time, before the number hit zero. That means 48 == 2^4 * 3^1
# Because divisors(n) = (a + 1)(b + 1)(c + 1)..., I can plug in 48 to get:
# divisors(48) = (4 + 1)(1 + 1) == 5 * 2 == 10
# Below is this algorithm put to code.

# This uses the same function from Problem 5, but omits the for loop and is_in_dictionary boolean tests
def get_prime_factor_occurrences(n):
    prime_factor_occurrences = {}

    # Get the only even prime out of the way; this is effectively a micro-optimization
    # in the context of this problem (see second while loop comment) since num_range will be a small number.
    # Were n to be a huge number, however, this optimization would start to prove useful
    i = 2
    count = 0

    while n % i == 0:
        count += 1
        n /= i  # 'n' here using /= changes its value inside the loop, but not the value of the 'n'
                # in the loop condition
    if count > 0:
        prime_factor_occurrences[i] = count

    # Now search for odd numbers; primes henceforth are exclusively odd so I can do i += 2
    i = 3

    while n != 1:
        count = 0
        while n % i == 0:
            count += 1
            n /= i

        if count > 0:
            prime_factor_occurrences[i] = count
        i += 2

    return prime_factor_occurrences

def get_num_divisors_2(n):
    prime_factor_occurrences = get_prime_factor_occurrences(n)
    num_divisors = 1

    for i in prime_factor_occurrences:
        num_divisors *= prime_factor_occurrences[i] + 1  # divisors(n) = (a + 1)(b + 1)(c + 1)...

    return num_divisors


triangle_value = 0
num_divisors = 0
i = 1

while num_divisors <= 500:
    triangle_value += i
    num_divisors = get_num_divisors_2(triangle_value)
    i += 1

print triangle_value, "has", num_divisors, "divisors."  # 76576500 has 576 divisors

# The above algorithm could be sped up by starting with a premade dictionary of primes and exponents for keys/values.
# These values, representing exponents, would be updated as new numbers are tested. This would be a more
# efficient approach because the method above has to create a new dictionary of primes for every successive
# triangle value. The issue with this solution, however, is that one will have to manually input an arbitrary
# dictionary size beforehand, and that size value (to my understanding) cannot be predetermined.
