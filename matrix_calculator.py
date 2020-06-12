import MartixMenager as MM

def main():
    menago = MM.MatrixMenger()
    functionalities = ("Adding_matrices", "Multiply_by_constant", "Multiply_by_matrix", "Transpose")
    while(True):
        menago.menu()
        choice = int(input("Your choice: "))
        if choice == 1:  # add marices
            menago.execute_function(functionalities[0])
        elif choice == 2:  # multiply by constatnt
            menago.execute_function(functionalities[1])
        elif choice == 3:  # multiply two matrices
            menago.execute_function(functionalities[2])
        elif choice == 4:  # transpose matrix
            pass
        else:
            break
        print()




main()