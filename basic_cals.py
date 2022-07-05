import numpy as npy

def add(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("A: \n", matrixA)
        print("B: \n", matrixB)
        return matrixA + matrixB

    except(ValueError):
        return "ERROR"

def substract(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("A: \n", matrixA)
        print("B: \n", matrixB)
        return matrixA - matrixB

    except(ValueError):
        return "ERROR"


def multiply(mtx, multiplier):
    try:
        matrix = npy.matrix(mtx)
        return matrix*multiplier

    except(ValueError):
        return "ERROR"


def divide(mtx, divisor):
    try:
        matrix = npy.matrix(mtx)
        result = matrix/divisor
        roundedMtx = npy.round(result, 3)
        return roundedMtx

    except(ValueError):
        return "ERROR"