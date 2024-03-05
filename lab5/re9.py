def j(x):
    res =""
    for c in x:
        if c.isupper():
            res+=" " + c
        else:
            res+=c
    return res
    
s =str(input())
print(j(s))