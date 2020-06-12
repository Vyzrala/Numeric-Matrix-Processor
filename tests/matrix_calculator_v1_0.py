def insert_matrix():
    rows, cols = input("Enter size of matrix: ").split()
    rows, cols = int(rows), int(cols)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        row = input().split()
        for j in range(cols):
            matrix[i][j] = float(row[j])
    
    return matrix


def display_result(matrix):
    if matrix == None: return
    dims = len(matrix), len(matrix[0])
    print("The result is: ")
    for i in range(dims[0]):
        row = map(lambda x: str(x), matrix[i])
        print(" ".join(row))



def add_matrices():
    first_matrix = insert_matrix()
    second_matrix = insert_matrix()
    dims_of_first = len(first_matrix), len(first_matrix[0])
    dims_of_second = len(second_matrix), len(second_matrix[0])
    if dims_of_first != dims_of_second:
        print("The operation cannot be performed.")
    else:
        for i in range(dims_of_first[0]):
            for j in range(dims_of_first[1]):
                second_matrix[i][j] += first_matrix[i][j]
        
        return second_matrix


def multiply_by_constant():
    matrix = insert_matrix()
    constant = float(input("Enter constant: "))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= constant
    
    return matrix


def multiply_two_matrices():
    first_matrix = insert_matrix()
    second_matrix = insert_matrix()
    dims_of_first = len(first_matrix), len(first_matrix[0])
    dims_of_second = len(second_matrix), len(second_matrix[0])
    if (dims_of_first[1] != dims_of_second[0]) and (dims_of_first[0]!= dims_of_second[1]):
        print("The operation cannot be performed.")
    else:
        result =  matrix = [[0 for _ in range(dims_of_second[1])] for _ in range(dims_of_first[0])]
        for i in range(dims_of_first[0]):
            for j in range(dims_of_second[1]):
                for k in range(dims_of_second[0]):
                    result[i][j] += first_matrix[i][k] * second_matrix[k][j]

        return result


def menu():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")


def main():
    while(True):
        menu()
        choice = int(input("Your choice: "))
        if choice == 1:
            display_result(add_matrices())
        elif choice == 2:
            display_result(multiply_by_constant())
        elif choice == 3:
            display_result(multiply_two_matrices())
        else:
            break
        print()

main()