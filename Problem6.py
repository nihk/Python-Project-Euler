# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 ? 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Brute-force it
def get_answer_1(upper_limit):
    square_sums = 0
    sum_squares = 0

    for i in range(1, upper_limit + 1):
        square_sums += i
        sum_squares += i * i

    square_sums *= square_sums

    return square_sums - sum_squares

print get_answer_1(100)  # 25164150

# More efficient solution integrating sum of natural numbers formula, n(n + 1) / 2, like Problem1.py did,
# but also the sum of squares formula n(n + 1)(2n + 1) / 6. These formulas make this problem quite trivial

def get_answer_2(upper_limit):
    square_sums = upper_limit * (upper_limit + 1) / 2
    square_sums *= square_sums
    sum_squares = upper_limit * (upper_limit + 1) * (2 * upper_limit + 1) / 6

    return square_sums - sum_squares

print get_answer_2(100)  # 25164150
