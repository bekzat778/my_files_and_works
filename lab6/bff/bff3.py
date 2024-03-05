def l(x)->str:
    return x == ''.join(reversed(x))
        
        
s = str(input())
print(l(s))