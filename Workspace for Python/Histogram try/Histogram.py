def transform(string_matrix):  # Use this matrix to change all the number in integer
    matrix = []
    for i in string_matrix:
        for j in i:
            if j == '\0':
                pass
            else:
                matrix = j


def histogram(matrix):
    data = {}
    for i in matrix:
        if data.has_key(i):
            data[i] += 1
        else:
            data[i] = 1
    return data

import os
f = open("matrix.txt", "r")
    #print(f.read())
matrix = input(f.read())
f.close("matrix.txt")
#matrix = open("matrix.txt")
print('234234\n', matrix)
#transform(matrix)
#a = histogram(matrix)
print(matrix,"sd")
#print(a)
