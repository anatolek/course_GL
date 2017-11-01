list_ = ["az", "toto", "picaro", "zone", "kiwi"]

def partlist(list_):
    return [(' '.join(list_[:x]), ' '.join(list_[x:])) for x in range(1,len(list_))]
    
print(partlist(list_))