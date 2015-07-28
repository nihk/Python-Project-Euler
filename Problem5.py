# #
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# #

# My original brute-force, very inefficient, but could be a lot worse. It starts with smallest_divisible equalling
# 20 and incrementing by 20 for each value that isn't divisible by all numbers 1 to 20. It also iterates from 20 until
# 2 in the for loop. The increment ensures that each number tested is certainly divisible by 20 and is more likely
# to fail as the for loop descends checking whether the number is divisible by 19, 18, and so on.

smallest_divisible = 20
is_divisible = False  # True if a number is divisible by all numbers 1 to 20

while not is_divisible:
    for i in range(20, 2, -1):
        is_divisible = smallest_divisible % i == 0
        if not is_divisible:
            smallest_divisible += 20
            break

print smallest_divisible  # 232792560

# Better approach. This problem has much in common with Problem3.py, which checks for prime factors. The number
# I am searching for will have to be divisible by all the prime factors of 20, i.e. 2, 3, 5, 7, 11, 13, 17, and 19,
# as per the fundamental theorem of arithmetic.
# The other non-prime values that must also divide into 20 to meet the requirements of this question,
# ie. 4, 6, 8, 10, 12, 14, 16, 18, 20 are each the products of some combination of the prime factors of 20,
# as I learned in Problem3.py.
#
# To account for this, I'll first express every number until 20 as a combination of its prime factors, (every
# number is divisible evenly by 1, so I'll start with 2):
# 2, 3, (2^2), 5, 2*3, 7, (2^3), 3^2, 2*5, 11, (2^2)*3, 13, 2*7, 3*5, (2^4), 17, 2*(3^2), 19, (2^2)*5
# The "2" with the highest exponent is four, i.e. 2^4 == 16, and the "3" with the largest exponent is two,
# i.e. 3^2 == 9.  Every other number from 1-20 is the product of four 2s or fewer, two 3s or fewer, and one of each
# of the remaining prime factors. I can reflect this in the array below. If I multiply every value in this array
# together, I will get the smallest number that is evenly divisible by every number from 1 to 20

smallest_divisible = 1
prime_factors = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]  # prime factors of 20

for i in prime_factors:
    smallest_divisible *= i

print smallest_divisible  # 232792560

# The above approach is much faster, but it isn't flexible because the array only works for numbers from 1-20.
# The method below enables any number range number input

# This function creates a dictionary of each prime factor <= num_range as key and a value as the greatest
# number of times the prime factor key could be divided into any number from 2 to num_range,
# e.g. 20 would have a prime factor key of 2, with a value of 4, since within num_range the number 16
# can be divided the most times by 2 compared to any other. This is the same as saying that
# for every 'n' from 2 to num_range (inclusive), the answer to log base 2 of 'n' is highest where n == 16, where
# the answer must be an integer
#
# get_prime_factor_occurrences() is based on what Problem3.py achieved.
def get_prime_factor_occurrences(num_range):
    prime_factor_occurrences = {}

    for i in range(2, num_range + 1):
        # Get the only even prime out of the way; this is effectively a micro-optimization
        # in the context of this problem (see second while loop comment) since num_range will be a small number.
        # Were num_range to be a huge number, however, this optimization would start to prove useful
        j = 2
        count = 0

        while i % j == 0:
            count += 1
            is_in_dictionary = j in prime_factor_occurrences
            # Only update a key's value if the count is greater than its current
            if not is_in_dictionary or (is_in_dictionary and count > prime_factor_occurrences[j]):
                prime_factor_occurrences[j] = count
            i /= j  # 'i' here using /= changes its value inside the loop, but not the value of the 'i'
                    # in the loop condition

        # Now search for odd numbers; primes henceforth are exclusively odd so I can do j += 2
        j = 3

        while i != 1:
            count = 0
            while i % j == 0:
                count += 1
                is_in_dictionary = j in prime_factor_occurrences
                if not is_in_dictionary or (is_in_dictionary and count > prime_factor_occurrences[j]):
                    prime_factor_occurrences[j] = count
                i /= j
            j += 2

    return prime_factor_occurrences

smallest_divisible = 1
prime_factors = get_prime_factor_occurrences(20)

for i in prime_factors:
    smallest_divisible *= i ** prime_factors[i]

print smallest_divisible  # 232792560
