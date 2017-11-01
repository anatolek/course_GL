def find_lambda(list_):
    for i in range(len(list_)):
        if type(list_[i]) is type(lambda: None):
            num = list_[i]
            del list_[i]
            break
    for j in range(len(list_)):
        list_[j] = num(list_[j])
    return list_

print(find_lambda([lambda a: a+2,9,3,1,0])) # [11, 5, 3, 2]
print(find_lambda([9,2,3,lambda a: a/2.0,1,0])) #[4.5, 1, 1.5, 0.5, 0.0]