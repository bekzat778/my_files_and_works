class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def area(self,w,le):
        self.w = w
        self.le = le
        return self.w * self.le
    
p = Rectangle()
print(p.area(5,15))