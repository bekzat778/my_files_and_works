import re 
k = str(input())
k = re.sub('[A-Z]','_',k)
l = list(map(str, k.split('_')))
print(l)