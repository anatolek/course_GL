#def test_me(*args, **kwargs):
#    pass
#    return True

s = "Invert me please"

def invert1 (x):
    x="".join(list(x)[::-1])
    return x
    
def invert2 (x):
    x="".join(reversed(x))
    return x

def invert3 (x):
    y=""
    for i in range (len(x)-1, -1, -1):
        y+=list(x)[i]
    return y

print (invert1 (s))
print (invert2 (s))
print (invert3 (s))