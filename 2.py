class Point:
    def __init__(self,stroka='0,0'):
        self.x=float(stroka[:stroka.index(',')])
        self.y=float(stroka[stroka.index(',')+1:])
        
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self,other):
        return Point(str(self.x+other.x)+','+str(self.y+other.y))
    def __sub__(self,other):
        return Point(str(self.x-other.x)+','+str(self.y-other.y))
    def russt_do_0(self):
        return (self.x**2+self.y**2)**0.5
N=int(input())
maximum=None
for i in range(N):
    A=Point(input())
    if maximum==None or A.russt_do_0()>maximum.russt_do_0():
        maximum=A
print(maximum)
