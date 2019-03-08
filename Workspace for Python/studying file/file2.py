"""
if you want to print ' or ", you have to write a \ before '
"""
import math
a=math.sin(2)
print(a)
name = input("please input your name")
a = len(name)
print(a)
if a>=10:
    print('your name is too long')
    print(name)
elif a < 10:
    print("your name is suitable")
    print("%s" % name)
    print('\n',name)
