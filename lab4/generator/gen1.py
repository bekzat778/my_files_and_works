import math 

def ll(b):
    a=0
    while a <= b:
        yield pow(a,2)
        a+=1
        
k = int(input())
print(list(ll(k)))



