import os



for i in range(1,27):
    j = chr(i+64)
    f = open(f'{j}.txt','x')
    f.close()