"""
" A palindromic number reads the same both ways. The largest palindrome made from the product of
" two 2-digit numbers is 9009 = 91 * 99.
"
" Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    i = 0
    j = len(num) - 1
    length = len(num)

    while (i < length / 2) and (j >= length - length / 2):
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1

    return True

# Alternate function that is more readable but runtime takes just as long (around 20-30 milliseconds) for
# this problem to complete.
def is_palindrome2(num):
    if num == num[::-1]:  # string[start:end(exclusive):step]
        return True
    else:
        return False

largest_palindrome = 0
d1 = 0
d2 = 0

# start at 999 and descend rather than 100 and ascend; the largest palindrome will certainly be a large number,
# so starting from the top means (most likely) fewer calls to is_palindrome()
for i in range (999, 100, -1):
    for j in range (i, 100, -1):
        product = i * j
        if product > largest_palindrome and is_palindrome(str(product)):
            d1 = i
            d2 = j
            largest_palindrome = product

print d1, '*', d2, '=', largest_palindrome  # 993 * 913 = 906609
