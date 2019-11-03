# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(
        os.getcwd(), 'python-workspace\\Workspace for Python\Calculator'))
    print(os.getcwd())
except:
    pass

# %%
import math


def p1(pn):
    return (pn*20+21/(pn*pn))/21


def p2(pn):
    return pn - (pow(pn, 3)-21)/(3*pn*pn)


def p3(pn):
    return pn - (pow(pn, 4)-21*pn)/(pn*pn-21)


def p4(pn):
    return math.sqrt(21/pn)


def p5(pn):
    # return 2+math.sin(pn)
    # return pow(x*pn + 5, 1/3)
    # return 1/3*pow(math.exp(1),pn/2)
    # return 1/2*pn +1/pn
    # return  pn - (-pow(pn,3) -math.cos(pn))/(-3*pn*pn +math.sin(pn))
    return pow(-pn, 3) - math.cos(pn)


def p6(x):
    return 4*pow(x, 2) - math.exp(x) - math.exp(-x)


def p7(x):
    return x - p6(x)/(8*x-math.exp(x)+math.exp(-x))


def p8(x):
    return x - (pow(x, 1/3))/(1/3*pow(x, -2/3))


# %%
def FixPoint(a, n, e):
    pn = Pn(a)

    for i in range(n):
        print(i+1, end="\t")
        pn_1 = Pn(pn)

        if (abs(pn - pn_1) < e):
            print("result = ", pn)
            return
        print(pn)

        pn = pn_1


def Pn(p):
    return p8(p)


# %%
FixPoint(1, 100, 0.00001)


# %%
FixPoint(-1, 100, 0.00001)


# %%
FixPoint(0, 100, 0.00001)


# %%
FixPoint(1, 100, 0.00001)


# %%
FixPoint(3, 100, 0.00001)


# %%
FixPoint(5, 100, 0.00001)


# %%
FixPoint(10, 100, 0.00001)


# %%
def SecondMethod(a, b, n, e):
    pn = Secant(a, b)
    pn_1 = b
    for i in range(n):
        print(i+2, end="\t")

        if (abs(pn - pn_1) < e):
            print("result = ", pn)
            return
        print(pn)
        temp = pn
        pn = Secant(pn, pn_1)
        pn_1 = temp


def Pn(p):
    return p5(p)


def Secant(x, y):
    return x - Pn(x)*(x-y)/(Pn(x)-Pn(y))


# %%
FixPoint(-1, 0, 1000, 0.001)


# %%
FixPoint(1, 3, 1000, 0.001)


# %%
FixPoint(1, 3, 1000, 0.001)


# %%
FixPoint(1, 3, 1000, 0.001)


# %%
FixPoint(1, 3, 1000, 0.001)
