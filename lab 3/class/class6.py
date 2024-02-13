class kot:
    def __init__(self,k)->int:
        self.k = k
    def oc(self):
        j = False
        for d in range(2,self.k):    
            x = lambda a,k: a % k == 0
            j = x(self.k,d)
        return j


g = int(input())
t = kot(g)
print(t.oc())
