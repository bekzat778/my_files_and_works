class Account:
    def __init__(self,b):
        self.b = b
    def sniat(self,s):
        self.s = s
        self.b = self.b - self.s
        return f"У вас осталось {self.b} тг"
    def popolnit(self,p):
        self.p = p
        self.b = self.b + self.p
        return f"У вас осталось {self.b} тг"
    def p():
        pass
    
print("Введите ваш баланс")
b = int(input())
ac = Account(b)
j = None
while j != "stop":
    print("Введите 1 для снятия или 2 для пополнения или чтобы остановить 0")
    j = int(input())
    if j ==0:
        break
    if j == 1:
        print("Сколько снимите...")
        x =int(input()) 
        print(ac.sniat(x))
    elif j ==2:
        print("Сколько пополните...")
        x = int(input())
        print(ac.popolnit(x))
    else:
        continue