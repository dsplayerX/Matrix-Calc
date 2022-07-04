import numpy as npy


def add(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("A: \n", matrixA)
        print("B: \n", matrixB)
        print("")
        return matrixA + matrixB

    except(ValueError):
        return "ERROR"

def substract(mtxA, mtxB):
    try:
        matrixA = npy.matrix(mtxA)
        matrixB = npy.matrix(mtxB)
        print("A: \n", matrixA)
        print("B: \n", matrixB)
        print("")
        return matrixA - matrixB

    except(ValueError):
        return "ERROR"


def multiply(mtx, multiplier):
    try:
        matrix = npy.matrix(mtx)
        return matrix*multiplier
    except(ValueError):
        return "ERROR"

def menu():
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("?.How to Use")

    option = input("Select option: ")
    
    if option == "1":
        userMtxA = input("Enter first matrix: ")
        userMtxB = input("Enter second matrix: ")
        print(add(userMtxA, userMtxB))
    
    elif option == "2":
        userMtxA = input("Enter first matrix: ")
        userMtxB = input("Enter second matrix: ")
        print(substract(userMtxA, userMtxB))

    elif option == "3":
        userMtx = input("Enter matrix: ")
        userMultiplier = int(input("Enter multiplier: "))
        print(multiply(userMtx, userMultiplier))

    elif option == "?":
        print("\nWhen entering matrices use spaces to differenciate elements in a row and ';' to differenciate columns")
        print("\n\t[[a b c]\n\t [j k l]\n\t [x y z]]")
        print("\nAbove matrix can be entered as an input as,")
        print("\ta b c; j k l; x y z")

menu()