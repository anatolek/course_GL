def narcissistic(test_number):
    if type(test_number) != int:
        return False
    sum_ = 0
    len_test_number = len(str(test_number))
    for i in str(test_number):
        sum_ += int(i)**len_test_number
    return sum_ == test_number