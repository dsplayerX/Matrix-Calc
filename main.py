import re
from basic_cals import *
from matrix_cals import *


def menu():

    isRunning = True

    while isRunning:
        print("\n1. Add")
        print("2. Substract")
        print("3. Multiply by constant")
        print("4. Divide by constant")
        print("5. Multiply Matrices")
        print("6. Transpose")
        print("7. Determinant")
        print("7. Inverse")

        print("?. How to Use")

        print("q. Quit")


        option = input("Select option: ").lower()
        
        if option == "1":
            userMtxA = input("Enter first matrix: ")
            userMtxB = input("Enter second matrix: ")
            result = add(userMtxA, userMtxB)
            print(result)

        elif option == "2":
            userMtxA = input("Enter first matrix: ")
            userMtxB = input("Enter second matrix: ")
            print(substract(userMtxA, userMtxB))

        elif option == "3":
            userMtx = input("Enter matrix: ")
            userMultiplier = int(input("Enter multiplier: "))
            result = multiply(userMtx, userMultiplier)
            print(result)

        elif option == "4":
            userMtx = input("Enter matrix: ")
            userDivisor = int(input("Enter divisor: "))
            result = divide(userMtx, userDivisor)
            print(result)

        elif option == "5":
            userMtxA = input("Enter first matrix: ")
            userMtxB = input("Enter second matrix: ")
            result = multiply_matrices(userMtxA,userMtxB)
            print("A.B:\n",result)

        elif option == "6":
            pass

        elif option == "7":
            pass

        elif option == "?":
            print("\nWhen entering matrices use spaces to differenciate elements in a row and ';' to differenciate columns")
            print("\n\t[[a b c]\n\t [j k l]\n\t [x y z]]")
            print("\nAbove matrix can be entered as an input as,")
            print("\ta b c; j k l; x y z")

        elif option == "q":
            isRunning = False


menu()