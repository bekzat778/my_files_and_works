from functools import reduce

def m(l)->list:
    return reduce(lambda x, y: x*y, l)
    
l = [5,88,9,5,4,8,4]
print(m(l))