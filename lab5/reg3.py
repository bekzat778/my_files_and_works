import re

p = r'[a-zA-Z0-9]+_[a-zA-Z0-9]+'

txt = str(input())

m = re.findall(p, txt)

print(m)