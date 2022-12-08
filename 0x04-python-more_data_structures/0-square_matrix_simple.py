#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = matrix.copy()
    for num in range(len(matrix)):
        square_matrix[num] = list(map(lambda x: x*x, matrix[num]))
    return (square_matrix)
