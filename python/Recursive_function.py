list_ = [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

def test_me(list_):
    if len(list_) == 0:
        return 0
    else:
        sum_ = 0
        for i in range(len(list_)):
            if type(list_[i]) == list:
                sum_ += test_me(list_[i])
            else:
                sum_ += list_[i]
        return sum_


# Writing the same using string processing
def test_me_(list_):
    if len(list_) == 0:
        return 0
    else:
        return sum([ float(x) for x in \
                str(list_).replace("[", "").replace("]", "").split(",") ])

print(test_me(list_))