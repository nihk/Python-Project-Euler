# The following iterative sequence is defined for the set of positive integers:
#
# n --> n/2 (n is even)
# n --> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Brute-force approach; tests every integer. I wrote this originally in Java and it found the answer in about
# two seconds, yet when rewritten with the same computational logic in Python it usually takes over thirty seconds!

longest_chain = 0
longest_chain_length = 0

for i in range(1, 1000000):
    j = i
    chain_length = 1  # All numbers are inherently a chain of length one

    while True:  # I did this originally in Java with a do-while loop.
        if j % 2 == 0:
            j /= 2
        else:
            j = 3 * j + 1

        chain_length += 1

        if j == 1:
            break

    if chain_length > longest_chain_length:
        longest_chain_length = chain_length
        longest_chain = i


# Longest chain starts on 837799 with a chain length of 525
print "Longest chain starts on", longest_chain, "with a chain length of", longest_chain_length


# The brute-force iterated over every integer and performed with a lot of redundancy. For example, in testing just the
# first three numbers it covered these:
# 1: 1. length = 1
# 2: 2 -> 1. length = 2
# 3: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1. length = 8
#
# After testing 3 it's already clear that:
# 10: length = 7
# 5: length = 6
# 16: length = 5
# 8: length = 4
# 4: length = 3
# 2: already tested; length was 2
# 1 already tested; length was 1
#
# Therefore, after testing the numbers 1, 2, and 3, the program shouldn't have to test any of the above numbers. The
# next number to be tested should be 6. That's 6: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1. length = 9. But as one
# can see, it overlaps with what was already calculated by testing the value 3. To get the chain length of 6, the
# program should only have to calculate the length of 3 plus 1 to get a length of 9.

collatz_chain_lengths = {}