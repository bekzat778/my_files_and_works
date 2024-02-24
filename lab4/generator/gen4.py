import math
def squares(x):
    for i in range(x+1):
        yield pow(i,2)

n = int(input())
print(list(squares(n)))