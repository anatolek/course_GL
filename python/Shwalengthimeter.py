test_strings = ["kawabunga", "metro2013", "moon", "orange"]
vowel = ("a", "e", "o", "i", "u", "y")

def shwalengthimter(x):
    for i in range (len(x)):
        k=len(x[i])
    # removing first character
        x[i]=x[i][1:]
    # removing next character if it is vowel
        for j in range(len(vowel)):
            if x[i][:1] == vowel[j]:
                x[i]=x[i][1:]
    # adding "shwa" to the beginning
        x[i]="shwa"+x[i]
    # adding " " (space) to the end
        x[i]+=" "
    # adding length of original string to the end
        x[i]+=str(k)
    return x

print(shwalengthimter(test_strings))