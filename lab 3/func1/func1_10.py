def unique(f)->list:
    s = set({})
    for i in f:
        s.add(i)
    return s
    

k = [1,1,2,4,5,8,7,9,4,1,2,6,4,5,6,4,58,7,4,5]
print(unique(k))
