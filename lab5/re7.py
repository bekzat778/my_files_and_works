import re


s = str(input())
l = ''
for i in range(len(s)):
    if s[i]=='_':
        l += s[i+1].upper()  
    else:
        l+=s[i]

l = re.sub('_','',l)
print(l)


