"""
" The prime factors of 13195 are 5, 7, 13 and 29.
"
" What is the largest prime factor of the number 600851475143 ?
"""

# The Fundamental theorem of arithmetic states that every positive integer greater than 1
# can be written as a product of prime numbers. That is to say that if I had a number, e.g. 36,
# that number is the product of some combination of prime numbers. The factors of 36, discluding 1 and itself,
# are 2, 3, 4, 6, 9, and 18. Each of those factors themselves can be factored further (discluding 1 and themselves).
# Factors of 4: 2. Factors of 6: 2, 3. Factors of 9: 3. Factors of 18: 2, 3, 6, 9. After factoring factors until
# it can be no longer continued without redundancy, it becomes clear that 36 is the product of some combination of
# 2s and 3s. It is 2 * 2 * 3 * 3. These are prime numbers and thus prime factors of 36, the largest being 3. These
# are guaranteed by the theorem to be prime numbers.
#
# I can apply this logic to this Project Euler problem. How? With the example I gave, 36, it becomes clear that I
# can divide it by 2 until division without a remainder is no longer possible, i.e. 36 / 2 = 18. 18 / 2 = 9.
# Division without a remainder no longer possible at 9. Increment the divisor to 3: 9 / 3 = 3.  3 / 3 = 1.
# 1 is not a prime number, therefore once the input becomes 1, the divisor I last used is the largest prime factor: 3.
# This neatly matches how I deduced in the first paragraph that 36 == 2 * 2 * 3 * 3; I divided by 2s twice and 3s also
# twice.

def get_largest_prime_factor(input):
    largest_prime_factor = 0
    i = 2  # my divisor, initialized as the smallest prime number, 2

    # 2 is the only even prime number possible, therefore if I get divide all I can by 2, then
    # in the second while loop I can use i += 2 since I know every potential prime factor above 2 will be odd.
    # Using i += 2 rather than i += 1 cuts out all the even numbers I know can never be prime
    while input % i == 0:
        largest_prime_factor = i
        input /= i

    i = 3  # divisor assigned the smallest odd prime number, 3

    while input != 1:
        while input % i == 0:  # no remainder after division, therefore input can be reduced
            largest_prime_factor = i
            input /= i  # keep reducing the input by division without remainders until no longer possible
        i += 2

    return largest_prime_factor

print get_largest_prime_factor(600851475143)  # 6857
