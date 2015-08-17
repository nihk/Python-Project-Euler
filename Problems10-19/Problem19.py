import calendar

# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def get_num_sundays(start_year = 1901, end_year = 2000):
    num_sundays = 0

    while start_year <= end_year:
        month = 1
        while month != 0:  # Once % 13 turns the month to zero, go to the next year
            if calendar.weekday(start_year, month, 1) is calendar.SUNDAY:
                num_sundays += 1
            month = (month + 1) % 13  # mod 13 to get the full 1-12 month range
        start_year += 1

    return num_sundays

print get_num_sundays()  # 171
