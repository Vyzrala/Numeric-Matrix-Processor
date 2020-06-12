from development import Matrix as mat

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
        matrix = mat.Matrix([int(x) for x in input("Enter size of matrix: ").split()])
        matrix.fill_matrix()
        self.matrix_array.append(matrix)

    def add_matrices(self):
        self.define_matrix()
        self.define_matrix()
        self.matrix_array[0].add_matrix(self.matrix_array[1])
        self.matrix_array[0].display()
        

