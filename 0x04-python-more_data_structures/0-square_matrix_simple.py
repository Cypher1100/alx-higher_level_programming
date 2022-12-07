#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for num in range(len(matrix)):
        squarematrix = list(map(lambda num: num*num,matrix[num]))
    return (squarematrix)
