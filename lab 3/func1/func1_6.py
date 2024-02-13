def rev(l)->list:
    return l[::-1]

f = input() 
k = f.split()
j = rev(k)
for i in j:
    print(i,end = ' ')