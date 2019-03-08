def change(aint,alis,adic):
    aint = 0
    alis.append(4)
    adict = {'apple':'34kg','blanana':'43kg','peach':'45kg','watermelon':'46kg'}
    print('In the changing:')
    print('aint: ',aint)
    print('alis: ',alis,' ;alist: ',alist);
    print('adic: ',adict,' ;adict: ',adict)

aint = 1
alist = [3]
adict = {'apple':34,'blanana':43,'peach':45,'watermelon':46}
print('Before used change:')
print('aint: ',aint)
print('alist: ',alist)
print('adict: ',adict)
change(aint,alist,adict)

print('After change:')
print('aint: ',aint)
print('alist: ',alist)
print('adict: ',adict)

'''
在函数中，如果改变list的参数将改变list的实参
但dictionary和int都不会改变实参
'''
