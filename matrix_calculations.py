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
        print("ERROR")


def substract(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("\nA: \n", matrixA)
        print("\nB: \n", matrixB)
        result = matrixA - matrixB
        print("\nA-B: \n", result)

    except(ValueError):
        print("ERROR")


def multiply(mtx, multiplier):
    try:
        matrix = npy.matrix(mtx)
        print("\nM:\n", matrix)
        result = matrix*multiplier
        print("\nM x", multiplier ,": \n", result)

    except(ValueError):
        print("ERROR")


def divide(mtx, divisor):
    try:
        matrix = npy.matrix(mtx)
        print("\nM:\n", matrix)
        result = matrix/divisor
        roundedMtx = npy.round(result, 3)
        result = roundedMtx
        print("\nM /", divisor ,": \n", result)

    except(ValueError):
        print("ERROR")
        

def multiply_matrices(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("\nA: \n", matrixA)
        print("\nB: \n", matrixB)
        result = npy.dot(matrixA, matrixB)
        print("\nA.B: \n",result)

    except(ValueError):
        print("ERROR")
    except(SyntaxError):
        print("Syntax Error")


def transpose(mtx):
    try:
        matrix = npy.matrix(mtx)
        print("\nM: \n", matrix)
        matrixTrans = matrix.transpose()
        print("\nMT: \n", matrixTrans)
    except(ValueError):
        print("ERROR")


def determinant(mtx):
    try:
        replacedMtx = mtx.replace("; ", "\n")
        ioMtx = StringIO(replacedMtx)
        matrix = npy.loadtxt(ioMtx)
        print("\nM: \n", matrix)
        matrixDet = npy.linalg.det(matrix)
        print("\ndetM: ", matrixDet)
    except(ValueError):
        print("ERROR")


def inverse(mtx):
    try:
        replacedMtx = mtx.replace("; ", "\n")
        ioMtx = StringIO(replacedMtx)
        matrix = npy.loadtxt(ioMtx)
        print("\nM: \n", matrix)
        matrixDet = npy.linalg.inv(matrix)
        print("\ninverse(M): \n", matrixDet)
    except(ValueError):
        print("ERROR")
