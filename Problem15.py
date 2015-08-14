# Starting in the top left corner of a 2 x 2 grid, and
# only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20 x 20 grid?

# Let r = "a right move" and d = "a down move." All possible combinations in the 2x2 grid, as provided by the
# problem itself, are: rrdd, rdrd, rddr, drrd, drdr, ddrr. It's clear I simply just need to get combinations of the
# "word" rrdd. This is the factorial of the length of that word, 4. 4! == 24. This isn't 6 because the letters r and
# d each have duplicates twice. There are 24 combinations of rrdd if I considered each letter unique, i.e. r1 r2 d1 d2.
# They aren't, however; I can deal with this by dividing 4! by the product of the factorial of the number of dupes, i.e.
# 4! / (2! * 2!). This gets me 6.
# In a 3x3 grid, one combination will be rrrddd. I just apply the logic above and I can deduce that 6! / (3! * 3!)
# means 20 different paths.
# For a 20x20 grid, I'd just use 40! / (20! * 20!). The formula for this problem can thus be simplified to:
# (n + n)! / (n! * n!) where n is a side-length of the square grid.

def get_factorial(n):
    product = 1
    while n != 1:
        product *= n
        n -= 1

    return product

def get_num_routes(side_length):
    a = side_length + side_length  # Length + width; the same as the number of right moves + down moves
    b = side_length

    a_fact = get_factorial(a)
    b_fact = get_factorial(b)

    num_routes = a_fact / (b_fact * b_fact)

    return num_routes


print get_num_routes(20)  # 137846528820
