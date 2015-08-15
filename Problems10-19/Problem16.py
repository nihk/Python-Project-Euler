# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

# Brute-force approach is also the best approach

n = 2 ** 1000
n_str = str(n)
sum_digits = 0

i = 0
while i < len(n_str):
    sum_digits += int(n_str[i])
    i += 1

print sum_digits  # 1366
