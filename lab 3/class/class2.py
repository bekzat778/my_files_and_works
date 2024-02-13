class Shape:
    def area(self):
        pass
    
class Square(Shape):
    def __init__(self,l):
        self.l = l
    def area(self):
        return self.l**2

p = Square(5)

print(p.area())