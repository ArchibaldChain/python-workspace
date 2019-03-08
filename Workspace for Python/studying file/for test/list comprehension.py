#list comprehension in Chinese is 推导或内涵
# [ < i 相关表达式> for i in aiterator]
#eg1
square = [i**i for i in range(1,11)]

'''
this codes has the same effect as the
/*
square = []
for i in range(1,11):
    square.append(i**i)
'''
print(square)

# eg2
key = ['apple','blanana','peach','watermelon']
value = ['34kg','43kg',45,4]
dictionary = { key:value for key,value in zip(key,value) }
for i,j in dictionary.items() :
    print(i,':',j)
