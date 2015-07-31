# The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832.
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

huge_number = '73167176531330624919225119674426574742355349194934' \
              '96983520312774506326239578318016984801869478851843' \
              '85861560789112949495459501737958331952853208805511' \
              '12540698747158523863050715693290963295227443043557' \
              '66896648950445244523161731856403098711121722383113' \
              '62229893423380308135336276614282806444486645238749' \
              '30358907296290491560440772390713810515859307960866' \
              '70172427121883998797908792274921901699720888093776' \
              '65727333001053367881220235421809751254540594752243' \
              '52584907711670556013604839586446706324415722155397' \
              '53697817977846174064955149290862569321978468622482' \
              '83972241375657056057490261407972968652414535100474' \
              '82166370484403199890008895243450658541227588666881' \
              '16427171479924442928230863465674813919123162824586' \
              '17866458359124566529476545682848912883142607690042' \
              '24219022671055626321111109370544217506941658960408' \
              '07198403850962455444362981230987879927244284909188' \
              '84580156166097919133875499200524063689912560717606' \
              '05886116467109405077541002256983155200055935729725' \
              '71636269561882670428252483600823257530420752963450'

# I went with a sliding calculation algorithm. To get the product of a number at indices 1-14 I simply
# need to divide the product of indices 0-13 by index 0 and multiply it by the number at index 14.
# This prevents a lot of redundant calculations compared to getting products from n to n + 13 indices by
# ignoring any of the previous calculations made. E.g. if one were to ask what the product of 5 * 6 * 7 * 8 is
# with the knowledge of what 4 * 5 * 6 * 7 is, it would be superfluous to just make the former calculation outright. One
# just needs to divide the product of 4 * 5 * 6 * 7 by 4 and multiply it by 8 to get the answer to 5 * 6 * 7 * 8.

def multiply_all_adjacent(n):
    product = 1
    i = 0
    while i < len(n):
        product *= int(n[i])
        i += 1

    return product

# Get the product of the first 13 digits
product = multiply_all_adjacent(huge_number[0:13])

# Helper variables
greatest_product = 0
greatest_product_adjacencies = 0  # The string of 13 numbers that made the greatest product
adjacent_limit = 13
first_pass_without_zero = True
i = 1  # The looping variable starts at 1 since the first thirteen were calculated already previously

# Shift the adjacent thirteen values over by dividing by the first digit and multiplying by the
# rightmost right neighbour. The presence of a 0 complicates matters and must be dealt with to
# prevent division by zero.

while i < len(huge_number) - adjacent_limit:
    small_number = huge_number[i:i + adjacent_limit]

    if not "0" in small_number:  # If it contains 0 it will yield a product of 0, so skip it
        if first_pass_without_zero:  # First time without a 0 product it needs to calculate all 13 adjacent digits
            product = multiply_all_adjacent(small_number)
            first_pass_without_zero = False
        else:
            product /= int(huge_number[i - 1])  # Divide by previous head
            product *= int(small_number[adjacent_limit - 1])  # Multiply by new end
    else:
        first_pass_without_zero = True

    if product > greatest_product:
        greatest_product = product
        greatest_product_adjacencies = small_number

    i += 1

# 5576689664895 made the product 23514624000
print greatest_product_adjacencies, "made the product", greatest_product