def l(x)->str:
    cu = 0
    cl = 0
    for i in x:
        if i.isupper():
            cu+=1
        elif i.islower:
            cl+=1
    return cu, cl
      
s = str(input())
print(l(s))