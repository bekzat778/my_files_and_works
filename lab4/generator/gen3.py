def g(x):
    a=0
    while a <= x:
        if (a%3==0 and a%4==0):
            yield a
        a+=1

n = int(input())
print(list(g(n)))