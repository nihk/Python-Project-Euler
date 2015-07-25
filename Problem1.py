"""
" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
" The sum of these multiples is 23.
"
" Find the sum of all the multiples of 3 or 5 below 1000.
"""

# My original brute-force approach
sum = 0

for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print sum   # 233168

# More efficient approach integrating the sum of natural numbers formula: n(n+1)/2
def sum_all_multiples(multiple, ceiling):
    reduced_ceiling = (ceiling - 1) // multiple  # ceiling - 1 because it's until the ceiling exclusive of last value
    return multiple * (reduced_ceiling * (reduced_ceiling + 1) / 2)

ceiling = 1000
# sum_all_multiples(15, ceiling) is subtracted since common factors of multiples of 3 and 5 will be added twice
# by the previous function calls
sum = sum_all_multiples(3, ceiling) + sum_all_multiples(5, ceiling) - sum_all_multiples(15, ceiling)

print sum   # 233168
