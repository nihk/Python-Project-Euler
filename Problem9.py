# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Brute-force approach
def print_pythagorean_triplet(limit):
    # limit / 3 because a < b < c
    for a in range(1, limit / 3):
        # limit / 2 because b < c
        for b in range(a + 1, limit / 2):
            # a + b + c always equals "limit" with this assignment to the variable "c"
            c = limit - a - b
            if a * a + b * b == c * c:
                print "The Pythagorean triplet is", a, ",", b, ", and", c
                print "Its product is", a * b * c
                return

# The Pythagorean triplet is 200 , 375 , and 425
# Its product is 31875000
print_pythagorean_triplet(1000)
