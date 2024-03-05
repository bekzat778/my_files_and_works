import os

os.unlink('/home/admin/Desktop/file/B.txt')

print(os.access('/home/admin/Desktop/file/B.txt',os.F_OK))