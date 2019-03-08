def fun(**adic):
     adic_origional = {'apple':'34','blanana':'43','peach':'45','watermelon':'46'}
     adic_origional.update(adic)
     print(adic_origional)

fun(apple='34kg',blanana='43kg',peach='45kg',watermelon='46kg')
"""
如果实参是dictionary中的一部分的话，定义的时候要加**
tuple和list用*
"""
