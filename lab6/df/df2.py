import os
print( os.access('/home/admin/Desktop/scripts1/scripts', os.F_OK))
print( os.access('/home/admin/Desktop/scripts1/scripts', os.R_OK))
print(os.access('/home/admin/Desktop/scripts1/scripts', os.W_OK))
print(os.access('/home/admin/Desktop/scripts1/scripts', os.X_OK))