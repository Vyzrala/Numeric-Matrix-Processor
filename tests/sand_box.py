class Matrix:
    determinant = None

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.shape = rows, cols
        self.matrix = self.support_matrix(rows, cols)

    def support_matrix(self, rows, cols):
        return [[0 for _ in range(cols)] for _ in range(rows)]

    def copy_martix(self, matrix):
        tmp = self.support_matrix(len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp[i][j] = matrix[i][j]
        return tmp

    def fill_matrix(self):
        print("Enter matrix values: ")
        for i in range(self.rows):
            row = input("> ").split()
            for j in range(self.cols):
                self.matrix[i][j] = float(row[j])
    
    def display(self, determinant=False):
        print("The result is: ")
        if determinant:
            print(self.determinant)
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    print(self.matrix[i][j], end=" ")
                print()

    def add_matrix(self, matrix):
        if self.shape != matrix.shape:
            print("The operation cannot be performed.")
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += matrix.matrix[i][j]
            return self

    def multipy_by_constant(self, constant):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] *= constant
        return self
    
    def multiply_by_matrix(self, matrix):
        if (self.cols != matrix.rows):
            print("The operation cannot be performed.")
        else:
            product = self.support_matrix(self.rows, matrix.cols)
            for i in range(self.rows):
                for j in range(matrix.cols):
                    for k in range(matrix.rows):
                        product[i][j] += self.matrix[i][k] * matrix.matrix[k][j]
            
            self.cols = matrix.cols
            self.shape = self.rows, matrix.cols
            self.matrix = product
            del product
            return self
    
    def transpose_main_diagonal(self):
        supp_matrix = self.support_matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                supp_matrix[j][i] = self.matrix[i][j]
        self.matrix = supp_matrix
        del supp_matrix
        return self

    def transpose_side_diagonal(self):
        supp_matrix = self.support_matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                supp_matrix[i][j] = self.matrix[self.cols - 1 - j][self.rows - 1 - i]
        self.matrix = supp_matrix
        del supp_matrix
        return self

    def transpose_vertical_line(self):
        supp_matrix = self.support_matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                supp_matrix[i][j] = self.matrix[i][self.cols - 1 - j]
        
        self.matrix = supp_matrix
        del supp_matrix
        return self

    def transpose_horizontal_line(self):
        supp_matrix = self.support_matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                supp_matrix[i][j] = self.matrix[self.rows - 1 - i][j]
        
        self.matrix = supp_matrix
        del supp_matrix
        return self

    def calculate_determinant(self, matrix=None, total=0):
        if matrix == None: matrix = self.matrix
        if len(matrix) == 2 and len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        
        indices = list(range(len(matrix)))
        for fc in indices:
            tmp_matrix = self.copy_martix(matrix)[1:]
            height = len(tmp_matrix)

            for i in range(height):
                tmp_matrix[i] = tmp_matrix[i][0:fc] + tmp_matrix[i][fc + 1:]

            sign = (-1) ** (fc % 2)
            sub_det = self.calculate_determinant(tmp_matrix)
            total += sign * matrix[0][fc] * sub_det

        self.determinant = total
        return total


class MatrixMenger:
    def __init__(self):
        self.matrix_array = []
    
    def main_menu(self):
        print("1. Add matrices\n2. Multiply matrix by a constant\n"+
        "3. Multiply matrices\n4. Transpose matrix\n"+
        "5. Calculate a determinant\n0. Exit")
    
    def transpose_menu(self):
        print("1. Main diagonal\n2. Side diagonal\n"+
        "3. Vertical line\n4. Horizontal line")
       
    def define_matrix(self):
        rows, cols = input("Enter matrix size: ").split()
        matrix = Matrix(int(rows), int(cols))
        matrix.fill_matrix()
        self.matrix_array.append(matrix)
    
    def execute_function(self, functionality):
        self.define_matrix()

        if functionality == "Adding_matrices":
            self.define_matrix()
            self.matrix_array[0].add_matrix(self.matrix_array[1])
        elif functionality == "Multiply_by_constant":
            constant = float(input("Enter constant: "))
            self.matrix_array[0].multipy_by_constant(constant)
        elif functionality == "Multiply_by_matrix":
            self.define_matrix()
            self.matrix_array[0].multiply_by_matrix(self.matrix_array[1])
        elif functionality == "Calculate_determinant":
            self.matrix_array[0].calculate_determinant()       
            self.matrix_array[0].display(determinant=True)
        else:
            print("Not know functionality.")
        
        if functionality != "Calculate_determinant":
            self.matrix_array[0].display()
        self.matrix_array = []
    
    def transpose_matrix(self):
        self.transpose_menu()
        choice = int(input("Your choice: "))
        if choice == 1:  # main diagonal
            self.define_matrix()
            self.matrix_array[0].transpose_main_diagonal()
        elif choice == 2:  # side diagonal
            self.define_matrix()
            self.matrix_array[0].transpose_side_diagonal()
        elif choice == 3:  # vertical line
            self.define_matrix()
            self.matrix_array[0].transpose_vertical_line()
        elif choice == 4:  # horizontal line
            self.define_matrix()
            self.matrix_array[0].transpose_horizontal_line()
        else:
            print("Invalid input.")
            return
        
        self.matrix_array[0].display()
        self.matrix_array = []


def main():
    menago = MatrixMenger()
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
            menago.execute_function(functionalities[4])
        else:
            break
        print()

main()