# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.
#
#     3
#    7 4
#   2 4 6
#  8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                                         75
#                                       95 64
#                                     17 47 82
#                                   18 35 87 10
#                                 20 04 82 47 65
#                               19 01 23 75 03 34
#                             88 02 77 73 07 63 67
#                           99 65 04 28 06 16 70 92
#                         41 41 26 56 83 40 80 70 33
#                       41 48 72 33 47 32 37 16 94 29
#                     53 71 44 65 25 43 91 52 97 51 14
#                   70 11 33 28 77 73 17 78 39 68 17 57
#                 91 71 52 38 17 14 91 43 58 50 27 29 48
#               63 66 04 68 89 53 67 30 73 16 69 87 40 31
#             04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
# Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute
# force, and requires a clever method! ;o)

# The solution is to start from the bottom. Add the nth index of the penultimate row to the nth index
# of the last row. Compare this result to the nth index of the penultimate row added to the n + 1 index of the last row.
# Whatever sum is the largest, the nth index of the penultimate row gets reassigned that larger sum. Do the same
# thing but last row -= 1 and penultimate row -= 1 until the peak of the triangle is the penultimate row.
# Whatever that peak is reassigned with by the algorithm will be the max path sum!
def get_max_path_sum(triangle):
    tri_copy = [row[:] for row in triangle]  # Preserve input

    for last_row in range(len(tri_copy) - 1, 0, -1):

        penultimate_row = last_row - 1

        for i in range(0, len(tri_copy[penultimate_row])):

            add_left  = tri_copy[penultimate_row][i] + tri_copy[last_row][i]
            add_right = tri_copy[penultimate_row][i] + tri_copy[last_row][i + 1]

            if add_left > add_right:
                tri_copy[penultimate_row][i] = add_left
            else:
                tri_copy[penultimate_row][i] = add_right

    return tri_copy[0][0]

# Changed 09 to 9 in the last row since all numbers prefixed with a zero are interpreted as octals, and 09 exceeds
# the limit of octals.
triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 04, 82, 47, 65],
    [19, 01, 23, 75, 03, 34],
    [88, 02, 77, 73, 07, 63, 67],
    [99, 65, 04, 28, 06, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
]

print get_max_path_sum(triangle)  # 1074
