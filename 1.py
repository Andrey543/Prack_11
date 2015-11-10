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
A=Point(input())
B=Point(input())
print(A+B,A-B)
