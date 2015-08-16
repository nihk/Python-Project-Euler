# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

def count_letters(limit = 1001):

    # I counted out each letter quantity by hand -- boring!
    numbers = {
        1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
        10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
        20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6,
        100: 7, 1000: 8,
        'and': 3
    }

    total_letters = 0

    for i in range(1, limit):
        if i < 20:
            total_letters += numbers[i]

        elif i < 100:
            tens_value = i - i % 10
            total_letters += numbers[tens_value]

            ones_value = i % 10
            # E.g. not 10, 20, 30, 40, etc.
            if ones_value > 0:
                total_letters += numbers[ones_value]

        elif i < 1000:
            hundreds_value = i / 100
            total_letters += numbers[hundreds_value]
            total_letters += numbers[100]

            ones_value = i % 10
            tens_value = (i % 100) - (i % 10)
            # E.g. not 100, 200, 300, etc.
            if ones_value > 0 or tens_value > 0:
                total_letters += numbers['and']

                # E.g 101 - 119, 201 - 219, etc.
                if i % 100 < 20:
                    total_letters += numbers[i % 100]

                # E.g. 120 - 199, 220 - 299, etc.
                else:
                    if tens_value > 0:
                        total_letters += numbers[tens_value]

                    if ones_value > 0:
                        total_letters += numbers[ones_value]

        elif i == 1000:
            total_letters += numbers[1]
            total_letters += numbers[1000]

    return total_letters


print count_letters()  # 21124


