import os

path = input()

if os.path.exists(path):
    print("exists")
    
    f = os.path.basename(path)
    d = os.path.dirname(path)
    
    print(f"Filename: {f}")
    print(f"Directory: {d}")
else:
    print("Path does not exist.")