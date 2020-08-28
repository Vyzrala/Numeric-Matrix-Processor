from Numeric_Matrix_Processor.MartixMenager import MatrixMenger


def main():
    menago = MatrixMenger()
    functionalities = ("Adding_matrices", "Multiply_by_constant",
                       "Multiply_by_matrix", "Transpose", "Calculate_determinant", "Inverse matrix")
    while True:
        menago.main_menu()
        choice = int(input("Your choice: "))
        print()
        if choice == 1:  # add matrices
            menago.execute_function(functionalities[0])
        elif choice == 2:  # multiply by constant
            menago.execute_function(functionalities[1])
        elif choice == 3:  # multiply two matrices
            menago.execute_function(functionalities[2])
        elif choice == 4:  # transpose matrix
            menago.transpose_matrix()
        elif choice == 5:  # calculate determinant
            menago.execute_function(functionalities[4])
        elif choice == 6:  # inverse matrix
            menago.execute_function(functionalities[5])
        else:
            break
        print()
