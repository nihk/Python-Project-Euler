import math

# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


# Brute-force; fast, even for an input of 1000, but it will do poorly with much larger inputs
def get_first_fib_index_with_n_digits(n=1000):
    if n == 1:
        return 0

    f0 = 0
    f1 = 1
    f2 = f0 + f1
    index = 2  # f2 is index 2
    num_digits = 0

    while num_digits != n:
        f0 = f1
        f1 = f2
        f2 = f0 + f1
        index += 1
        num_digits = len(str(f2))

    return index

print get_first_fib_index_with_n_digits()  # 4782


# More efficient means using a formula that calculates the number of digits in Fn
# At: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#fiblong
# the formula to get the number of digits of the nth fibonacci number is given as:
# round_down(N*LOG Phi - (LOG 5)/2) + 1
# where N is the fib index and Phi is the golden ratio.
# I can simply rearrange this to solve for the fib index like so:
def get_first_fib_index_with_num_digits(n=1000):
    PHI = 1.618033989  # approximately
    log_base = 10

    return math.ceil((n - 1 + math.log(5, log_base) / 2) / math.log(PHI, log_base))

print get_first_fib_index_with_num_digits()  # 4782.0
