import re 

pattern = r'a(b*)'

k = list(map(str, input().split()))

for s in k:
    m = re.search(pattern, s)
    if m:
        print(s)




