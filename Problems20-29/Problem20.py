# n! means n * (n - 1) * ... * 3 * 2 * 1
# 
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

def factorial(n):
    product = 1

    while n > 1:
        product *= n
        n -= 1

    return product

def sum_fact_digits(n):
    n_fact = str(factorial(n))
    sum_digits = 0

    for i in range(0, len(n_fact)):
        sum_digits += int(n_fact[i])

    return sum_digits


print sum_fact_digits(100)  # 648
