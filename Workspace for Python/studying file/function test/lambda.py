import math
s = lambda  x1,y1,x2,y2:math.sqrt((x1-x2)**2+(y1-y2)**2)
print(s(1,1,0,0))

a = (1,2,3,4)
b = (filter(lambda x:x % 2 == 0,a))
c = (map(lambda x:2*x,a))
print(b,'\n',c)
for i,j in zip(b,c):
    print(i,':',j)

def fun():
    pass         #pass没有任何作用
fun()
