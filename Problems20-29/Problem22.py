# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each
# name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?

def split_file(file_name):
    f = open(file_name)
    names = f.read().split(',')

    i = 0
    while i < len(names):
        names[i] = names[i][1:-1]  # Trims one character on both sides of a String, in this case, the quotation marks
        i += 1

    names.sort()

    return names

def get_name_score(rank, name):
    score = 0

    for i in name:
        score += ord(i.lower()) - 96

    return rank * score

def get_total_name_scores(file_name):
    names = split_file(file_name)
    total_scores = 0

    i = 0
    while i < len(names):
        # The first name entry should be a rank of 1, not zero, so the param will be 'i + 1' rather than just 'i'
        total_scores += get_name_score(i + 1, names[i])
        i += 1

    return total_scores

print get_total_name_scores('p022_names.txt')  # 871198282
