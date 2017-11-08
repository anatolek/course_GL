list1 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "123124", "message": "DB stopped! Whatta hell!", "datetime": 1474456391},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "1223134", "message": "U hev bin pwned by hax0r tim!", "datetime": 1474624799},
    {"id": "1213234", "message": "Need more vespene gas!", "datetime": 1474624791},
]

list2 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "3334113", "message": ""'; DELETE FROM customers WHERE 1 or username = '"; ", "datetime": 1474624789},
    {"id": "1213235", "message": "Require more minerals!", "datetime": 1474624792},
]


def merge_logs(list1, list2):
    resulted = sort_dict_key((list1 + list2), "id", True)
    resulted = sort_dict_key(resulted, "datetime")
    return resulted
    
def sort_dict_key(list_, dict_key, del_dublicate = False):
    key_list = [list_[x][dict_key] for x in range(len(list_))]
    if del_dublicate:
        sorted_index = dict.fromkeys([key_list.index(x) for x in sorted(key_list)]).keys()
    else:
        sorted_index = [key_list.index(x) for x in sorted(key_list)]
    return [list_[x] for x in sorted_index]

print(merge_logs(list1, list2))