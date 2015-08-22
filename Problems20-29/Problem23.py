# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Brute-force approach. This works but is fairly slow with large inputs; it takes about 15 seconds to do
# the required 28123 input.

def get_sum_proper_divisors(n):
    sum_proper_divisors = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            sum_proper_divisors += i
            if (i * i != n) and (i > 1):  # Avoid duplicate appends for perfect squares and n itself as a divisor
                sum_proper_divisors += n / i
        i += 1

    return sum_proper_divisors

def is_abundant_number(n):
    return get_sum_proper_divisors(n) > n

def get_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(1, limit):
        if is_abundant_number(i):
            abundant_numbers.append(i)

    return abundant_numbers

# Places every possible sum of two numbers in all the abundant numbers generated into a set
def get_sum_of_two_abundant_numbers(abundant_numbers):
    sum_abundant_number_pairs = set()
    i = 0
    while i < len(abundant_numbers):
        j = i
        while j < len(abundant_numbers):
            sum_abundant_number_pairs.add(abundant_numbers[i] + abundant_numbers[j])
            j += 1
        i += 1

    return sum_abundant_number_pairs

# Test every value from 1 to the limit and see if it's an abundant number.
def get_sum_non_abundants(limit):
    inclusive_limit = limit + 1
    abundant_numbers = get_abundant_numbers(inclusive_limit)
    sum_abundant_numbers = get_sum_of_two_abundant_numbers(abundant_numbers)
    sum_non_abundants = 0

    for i in range(1, inclusive_limit):
        if i not in sum_abundant_numbers:
            sum_non_abundants += i

    return sum_non_abundants


print get_sum_non_abundants(28123)  # 4179871


# A much more efficient approach tests for the presence of numbers that aren't the sum of two abundant numbers
# as it creates the set which contains abundant numbers. This uses the is_abundant_number() and
# get_sum_proper_divisors() functions from the brute-force approach.

def get_sum_non_abundant_numbers(limit):
    abundant_numbers = set()
    sum_non_abundants = 0

    for i in range(1, limit):
        if is_abundant_number(i):
            abundant_numbers.add(i)

        # Initialize this boolean as false, I'll presume that 'i' is not the sum of two abundant numbers.
        in_abundant_numbers = False

        for j in abundant_numbers:
            # If the difference of i - j is in the abundant_numbers set, then 'i' itself must be an abundant number.
            # E.g. let i = 30. At this point in time the abundant_numbers set will have tested every number from
            # 1-29 and determined that 12, 18, 20, and 24 are abundant numbers. I'll test every one of those values
            # against 'i': 30 - 24 = 6. Not in the set, 30 - 20 = 10. Not in the set. 30 - 18 = 12. This is in the
            # set, therefore 30 is indeed an abundant number.
            if i - j in abundant_numbers:
                in_abundant_numbers = True
                # Break because 'i' was found to be a sum of two abundant numbers in the set; no further
                # calculations are needed after the boolean is set.
                break

        if not in_abundant_numbers:
            sum_non_abundants += i

    return sum_non_abundants

print get_sum_non_abundant_numbers(28123)  # 4179871
