# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
# d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

# Brute-force approach
def d(n):
    proper_divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            proper_divisors.append(i)
            if (i * i != n) and (i > 1):  # Avoid duplicate appends for perfect squares and n itself as a divisor
                proper_divisors.append(n / i)
        i += 1

    return sum(proper_divisors)

def get_sum_amicable_pairs(limit):
    sum_pairs = 0

    for a in range(1, limit):
        b = d(a)
        if a == d(b) and a != b:
            sum_pairs += a

    return sum_pairs


print get_sum_amicable_pairs(10000)  # 31626
