import math
def poly(x,y):
    c = x * pow(y,2)
    a = 4 * math.tan(math.pi / x)
    return round(c / a)

x = int(input())
y = int(input())
print(poly(x,y))