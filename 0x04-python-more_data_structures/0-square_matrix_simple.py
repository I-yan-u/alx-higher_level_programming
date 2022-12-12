#!/usr/bin/python3
def square_row(row=[]):
    rnMat = []
    for num in row:
        rnMat.append(num**2)
    return rnMat


def square_matrix_simple(matrix=[]):
    nMat = []
    for row in matrix:
        nMat.append(square_row(row))
    return nMat
