import numpy as np
import math

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.

'''Below is the method that is thought by myself'''
# def cross_entropy(Y, P):
#     crossEntropy = 0
#     for i in range(len(Y)):
#         crossEntropy -= Y[i] * math.log(P[i]) + (1 - Y[i]) * math.log(1 - P[i])
#     return crossEntropy
#     pass
"""
Below is the right way to calculate cross_entropy
"""
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
