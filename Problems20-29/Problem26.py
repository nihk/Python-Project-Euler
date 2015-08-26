# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
#     denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
# recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


# I originally tried to brute-force this by testing subtrings using pattern matching, but there were too many
# indeterminate factors, e.g. how long should the decimals run for to test for a pattern? Upon finding through
# research online that the answer was a 982 length pattern, I knew my original intention would never work
# in a realistic amount of time.

# I'm interested in the cases where the denominator has no factor 2 or 5, i.e. ends in a digit 1, 3, 7, or 9, because
# factors 2 and 5 in the denominator change neither the period length nor the sequence of digits in the period.
# E.g. 1/2 = 0.5, 1/4 = 0.25, 1/8 = 0.125, 1/5 = 0.2. These all have no period whatsoever.
# For denominator i, the period length is the smallest j such that i divides (10^j) - 1.
# Source: http://hr.userweb.mwn.de/numb/period.html
#
# I can use this information to solve the problem quite simply. Take the number 7 for example. This isn't
# evenly divisible by 2 or 5, so it's a valid candidate to test for period length. Starting with j = 1, I want
# to test increasing values of j for 10^j - 1 until the answer to that, mod 997, is equal to zero.
# E.g.
# (10^1 - 1) % 7 = 2
# (10^2 - 1) % 7 = 1
# (10^3 - 1) % 7 = 5
# etc., until I find that
# (10^6 - 1) % 7 = 0
# This means that a denominator of 7 creates a period length of 6.
# I can simplify the calculation further by stating that j is the period length of i when 10^j % i == 1 and
# j is the smallest possible.
#
# Why does this method work? Take the period of 1/7, for example: 142857.
# 10^j - 1 divided by 7 will be the value of that period itself for certain values of j. In this case,
# 10^6 - 1 / 7 is the same as 999999 / 7 which equals 142857, and 142857/999999 is simplified to 1/7.
#
# Sometimes a prime will have a period length of its own value minus 1, as was the case with 7, which has a period
# length of 7 - 1. Therefore, checking from 999 to 1 would likely find the denominator with the longest period length
# earlier than starting from 1 to 999.

longest_period = 0
longest_period_denominator = 0

# NB: 'i' should always be greater than 1 for this problem; if it were assigned 1, it would loop infinitely inside
# its nested loop checking 10 ** j % 1, which will always equal zero for any value of 'j'.
for i in range(999, 1, -1):
    j = 1

    while i % 2 != 0 and i % 5 != 0 and 10 ** j % i != 1:
        j += 1

        if j > longest_period:
            longest_period = j
            longest_period_denominator = i

    i -= 1

print longest_period_denominator, 'produced a period length of', longest_period  # 983 produced a period length of 982
