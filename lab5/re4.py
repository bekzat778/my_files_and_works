import re

pat = r'\b[A-Z][a-z]'

k = list(map(str, input().split()))
for i in k:
    m = re.search(pat, i)
    if m:
        print(i)