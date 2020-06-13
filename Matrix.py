class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.shape = rows, cols
        self.matrix = self.support_matrix(rows, cols)

    def support_matrix(self, rows, cols):
        return [[0 for _ in range(cols)] for _ in range(rows)]

    def fill_matrix(self):
        print("Enter matrix values: ")
        for i in range(self.rows):
            row = input("> ").split()
            for j in range(self.cols):
                self.matrix[i][j] = float(row[j])
    
    def display(self):
        print("The result is: ")
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
