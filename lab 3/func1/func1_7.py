def three(k)->list:
    t = False
    for i in range(len(k)):
        if i !=len(k)-1:
            if (k[i]==3 and k[i+1]==3):
                t = True
    return t

g = []
j = int(input())
for i in range(j):
    l = int(input())
    g.append(l)


print(three(g))
            