import time
import math

def s(n, mil):
    time.sleep(mil/1000)
    res = math.sqrt(n)
    return f"Square root of {n} after {mil} milliseconds is {res}"
    

o = int(input())
j = int(input())
print(s(o,j))