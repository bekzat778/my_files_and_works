import os

f = open('/home/admin/Desktop/scripts1/scripts','r')
h = f.read()
f.close()
t = open('/home/admin/Desktop/file/A.txt','w')
t.write(h)
t.close()
