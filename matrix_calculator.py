import MartixMenager as MM

def main():
    menago = MM.MatrixMenger()
    functionalities = ("Adding_matrices", "Multiply_by_constant",
     "Multiply_by_matrix", "Transpose", "Calculate_determinant")
    while(True):
        menago.main_menu()
        choice = int(input("Your choice: "))
        print()
        if choice == 1:  # add marices
            menago.execute_function(functionalities[0])
        elif choice == 2:  # multiply by constatnt
            menago.execute_function(functionalities[1])
        elif choice == 3:  # multiply two matrices
            menago.execute_function(functionalities[2])
        elif choice == 4:  # transpose matrix
            menago.transpose_matrix()
        elif choice == 5:  # calculate determinant
            pass
        else:
            break
        print()

main()