x = [int(input('please input a integer: ')), int(input('please input a integer: '))]
x1 = min(x)
x2 = max(x)
import math
a = int(math.sqrt(x2))
for i in range(x1, x2+1):
    print(i)
    for j in range(2, a+1):
        if i%j == 0:
            if j == 2:   #判断是否为偶
                b = 2
            print(i,'is not prime number.',b)
            break
    else:
        print(i, end=' ')
    if i % 100 == 0:
        print('\n')
