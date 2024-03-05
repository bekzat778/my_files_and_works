import re
s = str(input())


m = re.sub(r'[., ]', ':',s)
    

print(m)