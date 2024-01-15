#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [[col[i] ** 2 for i in range(len(col))] for col in matrix]
