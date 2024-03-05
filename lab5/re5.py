import re

pat = r'\ba*b\b'

k = list(map(str, input().split()))
for i in k:
    m = re.findall(pat, i)
    if m:
        print(i)