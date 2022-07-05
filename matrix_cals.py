import numpy as npy


def multiply_matrices(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("A: \n", matrixA)
        print("B: \n", matrixB)
        result = npy.dot(matrixA, matrixB)
        return(result)
    except(ValueError):
        return "ERROR"
    except(SyntaxError):
        return "Syntax Error"


def inverse(matrix):
    pass
