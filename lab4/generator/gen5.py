def i(x):
    a=0
    while x >=a:
        yield x
        x-=1

n=int(input())
print(list(i(n)))