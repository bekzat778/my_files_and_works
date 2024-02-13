class all():
    def getstring(self,x)->str:
        self.x = x
    def printString(self):
        return self.x.upper()

p = all()
l = "dkwoa"
k = p.getstring(l) 
print(p.printString())