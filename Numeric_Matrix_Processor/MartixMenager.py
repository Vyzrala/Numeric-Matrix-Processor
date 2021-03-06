from Numeric_Matrix_Processor.Matrix import Matrix


class MatrixMenger:
    def __init__(self):
        self.matrix_array = []

    def main_menu(self):
        print("1. Add matrices\n2. Multiply matrix by a constant\n" +
              "3. Multiply matrices\n4. Transpose matrix\n" +
              "5. Calculate a determinant\n6. Inverse matrix\n0. Exit")

    def transpose_menu(self):
        print("1. Main diagonal\n2. Side diagonal\n" +
              "3. Vertical line\n4. Horizontal line")

    def define_matrix(self):
        rows, cols = input("Enter matrix size: ").split()
        matrix = Matrix(int(rows), int(cols))
        matrix.fill_matrix()
        self.matrix_array.append(matrix)

    def execute_function(self, functionality):
        self.define_matrix()
        ret_value = 1
        if functionality == "Adding_matrices":
            self.define_matrix()
            self.matrix_array[0].add_matrix(self.matrix_array[1])
        elif functionality == "Multiply_by_constant":
            constant = float(input("Enter constant: "))
            self.matrix_array[0].multiply_by_constant(constant)
        elif functionality == "Multiply_by_matrix":
            self.define_matrix()
            self.matrix_array[0].multiply_by_matrix(self.matrix_array[1])
        elif functionality == "Calculate_determinant":
            self.matrix_array[0].calculate_determinant()
            self.matrix_array[0].display(det=True)
        elif functionality == "Inverse matrix":
            ret_value = self.matrix_array[0].calculate_inverse_matrix()
        else:
            print("Not know functionality.")

        if functionality != "Calculate_determinant" and ret_value != -1:
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
