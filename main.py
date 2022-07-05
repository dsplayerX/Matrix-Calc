from matrix_calculations import *

def menu():

    isRunning = True

    while isRunning:
        print("-------------------")
        print(" MATRIX CALCULATOR ")
        print("-------------------")
        print("  1. Add")
        print("  2. Substract")
        print("  3. Multiply (by a constant)")
        print("  4. Divide (by a constant)")
        print("  5. Multiply Matrices")
        print("  6. Transpose")
        print("  7. Determinant")
        print("  8. Inverse")
        print("-------------------")
        print("  ?. How to Use")
        print("-------------------")
        print("  q. Quit")

        option = input("Select option: ").lower()
        
        if option == "1": # Addition
            userMtxA = input("Enter first matrix: ")
            userMtxB = input("Enter second matrix: ")
            add(userMtxA, userMtxB)
            
        elif option == "2": # Substraction
            userMtxA = input("Enter first matrix: ")
            userMtxB = input("Enter second matrix: ")
            substract(userMtxA, userMtxB)

        elif option == "3": # Multiplication by constant
            userMtx = input("Enter matrix: ")
            userMultiplier = int(input("Enter multiplier: "))
            multiply(userMtx, userMultiplier)

        elif option == "4": # Division by constant
            userMtx = input("Enter matrix: ")
            userDivisor = int(input("Enter divisor: "))
            divide(userMtx, userDivisor)

        elif option == "5": # Matrice Multiplication
            userMtxA = input("Enter first matrix: ")
            userMtxB = input("Enter second matrix: ")
            multiply_matrices(userMtxA,userMtxB)
            
        elif option == "6": # Transpose
            userMtx = input("Enter matrix: ")
            transpose(userMtx)

        elif option == "7": # Determinant
            inputMtx = input("Enter matrix: ")
            determinant(inputMtx)

        elif option == "8": # Inverse
            inputMtx = input("Enter matrix: ")
            inverse(inputMtx)

        elif option == "?":
            print("\nWhen entering matrices use a <Space> \nto differenciate elements in a row \nand ';' after each row to differenciate rows")
            print("\n\t[[a b c]\n\t [j k l]\n\t [x y z]]")
            print("\nAbove matrix can be entered as an input as,")
            print("\n\ta b c; j k l; x y z")

        elif option == "q":
            isRunning = False
        
        else:
            print("Wrong input! Try again!")


menu()