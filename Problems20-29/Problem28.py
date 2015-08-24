# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


# I originally wanted to build the 1001x1001 spiral grid in a two dimensional array, but a convenient means of
# doing so escaped me. Instead, I just noted the patterns along each NE, NW, SW, and SE diagonal; each was a sequence
# starting on 1 with a unique interval. Each successive interval, however, was always 8 more than the previous for
# each diagonal.

def get_sum_diagonals(grid_size=1001):
    if grid_size % 2 == 0:
        return 'Grid must be of an odd dimension size.'

    # Initialize each diagonal as the center node. This value will change immediately in the for loop, with respect
    # to each diagonal interval
    ne_diagonal_value, nw_diagonal_value, sw_diagonal_value, se_diagonal_value = [1] * 4
    global_interval = 8
    sum_diagonals = 1  # Initialize as the center node

    i = 1
    while i <= grid_size / 2:
        # Each will be subtracted by a constant (except NE); this simply adheres to the pattern found along
        # each diagonal
        ne_diagonal_value += i * global_interval
        nw_diagonal_value += i * global_interval - 2
        sw_diagonal_value += i * global_interval - 4
        se_diagonal_value += i * global_interval - 6

        sum_diagonals += ne_diagonal_value + nw_diagonal_value + sw_diagonal_value + se_diagonal_value
        i += 1

    return sum_diagonals


print get_sum_diagonals()  # 669171001
