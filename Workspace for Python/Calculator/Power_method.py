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
import numpy as np
# %% [markdown]
# ### Power method
# > to  calculate the largest eigenvale and corresponing egienvalue.
# %%
# defind the power method.


def power_method(A, x, TOL, N):
    # n dimension, A matrix, x vector, TOL tolerance,  N maximum number of iteration
    # step 1
    k = 1
    A = np.matrix(A)
    # step 2
    x = np.array(x)
    x_p = max(np.abs(x))
    p = indexOf(np.abs(x), x_p)
    # step 3
    x = x/x_p
    # step 4
    for i in range(N):
        print(i, x)
        # step 5
        y = np.array(np.multiply(A, x))
        # step 6
        miu = y[p]
        # step 7
        y_p = min(np.abs(y))
        p = indexOf(np.abs(y), y_p)
        # step 8
        if y[p] == 0:
            print('Eignevector', x)
            print('A has the eigenvaleu 0, select a new vector x')
            return 0, x
        # step 9
        ERR = np.max(np.abs(x - y/y_p))
        x = y/y_p
        # step 10
        if ERR < TOL:
            print(miu, x)
            return miu, x
    print('The maximum number of iterations exceeded')
    return


def indexOf(x, a):
    for i in range(len(x)):
        if x[i] == a:
            return i
    return None


# %%
A = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
x = [1, -1, 2]
power_method(A, x, 0.2, 3)
