import Matrix as mat

class MatrixMenger:
    def __init__(self):
        self.matrix_array = []
    
    def menu(self):
        print("""
        1. Add matrices
        2. Multiply matrix by a constant
        3. Multiply matrices
        4. Transpose matrix
        0. Exit""")
    
    def define_matrix(self):
        rows, cols = input("Enter matrix size: ").split()
        matrix = mat.Matrix(int(rows), int(cols))
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
        else:
            print("Not know functionality.")
            
        self.matrix_array[0].display()
        self.matrix_array = []
