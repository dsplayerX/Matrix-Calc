from io import StringIO 
import numpy as npy

def add(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("\nA: \n", matrixA)
        print("\nB: \n", matrixB)
        result = matrixA + matrixB
        print("\nA+B: \n", result)

    except(ValueError):
        print("ERROR: User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")


def substract(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("\nA: \n", matrixA)
        print("\nB: \n", matrixB)
        result = matrixA - matrixB
        print("\nA-B: \n", result)

    except(ValueError):
        print("ERROR: User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")


def multiply(mtx, multiplier):
    try:
        matrix = npy.matrix(mtx)
        print("\nM:\n", matrix)
        result = matrix*multiplier
        print("\nM x", multiplier ,": \n", result)

    except(ValueError):
        print("ERROR: User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")


def divide(mtx, divisor):
    try:
        matrix = npy.matrix(mtx)
        print("\nM:\n", matrix)
        result = matrix/divisor
        roundedMtx = npy.round(result, 3)
        result = roundedMtx
        print("\nM /", divisor ,": \n", result)

    except(ValueError):
        print("ERROR: User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")
        

def multiply_matrices(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("\nA: \n", matrixA)
        print("\nB: \n", matrixB)
        result = npy.dot(matrixA, matrixB)
        print("\nA.B: \n",result)

    except(ValueError):
        print("ERROR!")
        print("Could be because,")
        print("  The number of columns in the first matrix are not equal to the number of rows in the second matrix.\n  User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")
    except(SyntaxError):
        print("Syntax Error")


def transpose(mtx):
    try:
        matrix = npy.matrix(mtx)
        print("\nM: \n", matrix)
        matrixTrans = matrix.transpose()
        print("\nMT: \n", matrixTrans)
    except(ValueError):
        print("ERROR: User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")


def determinant(mtx):
    try:
        replacedMtx = mtx.replace("; ", "\n")
        ioMtx = StringIO(replacedMtx)
        matrix = npy.loadtxt(ioMtx)
        print("\nM: \n", matrix)
        matrixDet = npy.linalg.det(matrix)
        print("\ndetM: ", matrixDet)
    except(ValueError):
        print("ERROR: User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")


def inverse(mtx):
    try:
        replacedMtx = mtx.replace("; ", "\n")
        ioMtx = StringIO(replacedMtx)
        matrix = npy.loadtxt(ioMtx)
        print("\nM: \n", matrix)
        matrixDet = npy.linalg.inv(matrix)
        print("\ninverse(M): \n", matrixDet)
    except(ValueError):
        print("ERROR: User input is not a matrix.\nSelect '?' in menu to read how to enter a matrix")
    except(npy.linalg.LinAlgError):
        print("ERROR: Matrix should be a square matrix.")
