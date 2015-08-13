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

def get_collatz_chains(limit):
    collatz_chain_lengths = {}
    collatz_numbers = []

    for i in range(1, limit):
        # If 'i' isn't in the dictionary, add it, otherwise just continue to the next 'i' value
        if i not in collatz_chain_lengths:
            # All chains start with a length of 1
            collatz_chain_lengths[i] = 1
            # This collatz_numbers array is needed to remember what the previous collatz number was. I can't
            # get the previous collatz simply by inversing the n /= 2 or n = 3n + 1 because with even numbers
            # it's impossible to tell what the previous collatz was. E.g. for 8, the previous number might've
            # been 16 [16 / 2 == 8] or 2.33~ [3 * 2.33~ + 1 == 8]. This array instead just remembers exactly what
            # that previous collatz number was.
            collatz_numbers.append(i)

            # 'j' is assigned the value of 'i' so it can test through its chain while 'i' is preserved
            j = i
            # Perform chain calculation
            while j != 1:
                if j % 2 == 0:
                    j /= 2
                else:
                    j = 3 * j + 1

                if j not in collatz_chain_lengths:
                    # Iterate backwards through the history of collatz numbers, adding one to each previous key until
                    # the key is equal to the 'i' value being tested.
                    # E.g. for the number 3 the chain is:
                    # 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 [2 is in dictionary, so end here]
                    # The dictionary updates like so:
                    # 3: 1
                    # 3: 2, 10: 1
                    # 3: 3, 10: 2, 5: 1
                    # etc., until:
                    # 3: 6, 10: 5, 5: 4 , 16: 3, 8: 2, 4: 1
                    # ***NB, the above values in this current state are incorrect; this is fixed by the "else"
                    # of this if/else statement, see "else" comment below.
                    for k in reversed(collatz_numbers):
                        collatz_chain_lengths[k] += 1
                        if k == i:
                            break

                    # I only need to store numbers < limit
                    if j < limit:
                        collatz_chain_lengths[j] = 1
                        collatz_numbers.append(j)

                # if 'j' is in collatz_chain_lengths already, then I just need to add that chain length value
                # and not iterate redundantly through them all with += 1
                # Therefore, with the example of 3, the key 2 was already in the dictionary, so I add the value of
                # that key to everything previously on the chain that 3 had. So:
                # 3: 6 + 2, 10: 5 + 2, 5: 4 + 2 , 16: 3 + 2, 8: 2 + 2, 4: 1 + 2
                else:
                    for k in reversed(collatz_numbers):
                        collatz_chain_lengths[k] += collatz_chain_lengths[j]
                        if k == i:
                            break
                    # Break the while loop because all further values of 'j' have already been determined
                    break

    return collatz_chain_lengths

def print_longest_collatz_chain(limit):
    collatz_chain_lengths = get_collatz_chains(limit)

    longest_chain = 0
    longest_chain_length = 0

    for i in collatz_chain_lengths:
        if collatz_chain_lengths[i] > longest_chain_length:
            longest_chain = i
            longest_chain_length = collatz_chain_lengths[i]

    print longest_chain, 'had the longest chain with a length of', longest_chain_length


# 837799 had the longest chain with a length of 525
print_longest_collatz_chain(1000000)