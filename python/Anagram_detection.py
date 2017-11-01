def is_anagram(test, original):
    if len(test) != len(original):
        return False
    return sorted(test.lower()) == sorted(original.lower())
    
print(is_anagram('Buckethead', 'DeathCubeK'))   #True
print(is_anagram('B1  f', 'F  b1'))             #True
print(is_anagram('python', 'ruby'))             #False
print(is_anagram('python', 'golang'))           #False