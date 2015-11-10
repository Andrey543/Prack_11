class Point:
    def __init__(self,stroka='0,0',mass=1):
        self.x=float(stroka[:stroka.index(',')])
        self.y=float(stroka[stroka.index(',')+1:])
        self.mass=mass
        
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self,other):
        return Point(str(self.x+other.x)+','+str(self.y+other.y))
    def __sub__(self,other):
        return Point(str(self.x-other.x)+','+str(self.y-other.y))
    def russt(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def c_mass(self,other):
        x=self.x+(other.x-self.x)/(self.mass+other.mass)
        y=self.y+(other.y-self.y)/(self.mass+other.mass)
        return Point(str(x)+','+str(y),self.mass+other.mass)
N=int(input())
A=Point(input())
for i in range(N-1):
    B=Point(input())
    if B.mass<A.mass:
        B,A=A,B
    A=B.c_mass(A)
print(A)


        
