import math

def k(x):
    a=0
    while a <= x:
        if a%2==0:
            yield a
        a+=1

n = int(input())
print(list(k(n)))