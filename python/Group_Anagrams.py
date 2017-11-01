test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]


def groupAnagrams(input_list):

    output_list = []
    while len(input_list):
        
        i = 0
        temp_list = [input_list[0]]
        del input_list[0]

        while i < len(input_list):
            if is_anagram(temp_list[0], input_list[i]):
                temp_list.append(input_list[i])
                del input_list[i]
            else:
                i += 1
        output_list.append(temp_list)
        
    return output_list


def is_anagram(test, original):
    if len(test) != len(original):
        return False
    return sorted(test.lower()) == sorted(original.lower())