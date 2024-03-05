import re 

p = 'abb'
p1 = 'abbb'
k = list(map(str, input().split()))

for s in k:
    m = re.search(p, s)
    m1 = re.search(p1, s)
    if (m or m1):
        print(s)
