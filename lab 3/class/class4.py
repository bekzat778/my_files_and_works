class Point:
    def show(self,x,y) ->int:
        self.x= x
        self.y = y
        return self.x,self.y
    def move(self,k,l)->int:
        self.k = k
        self.l = l
        return self.k, self.l
    def dist(self):
        o = (self.x - self.k)**2 + (self.y - self.l)**2
        return pow(o,0.5)

       
g = Point()
g1 = g.show(8, 9)
g2 = g.move(5,6)
print(g1)
print(g2)
print(g.dist())