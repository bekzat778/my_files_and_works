def prime(l)->list:
    h = []
    for i in l:
        k = True
        for j in range(2,i):
            if i%j==0:
                k = False
        if k:
            h.append(i)

g = [1,8,6,7,4,8,9,5]
print(g)