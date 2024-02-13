def zero(k)->list:
    l = False
    for i in range(len(k)):
        if i != len(k)-2:
            if (k[i]==0 and k[i+1]==0 and k[i+2]==7):
                l = True
    return l

li = []
t = int(input())
for i in range(t):
    g = int(input())
    li.append(g)

print(zero(li))
