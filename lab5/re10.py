def l(x):
    res = ""
    for c in x:
        if c.isupper():
            res+='_' + c.lower()
        else:
            res+=c
            
    return res
    
s = str(input())
print(l(s))