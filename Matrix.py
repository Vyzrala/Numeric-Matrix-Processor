import math

class Matrix:
    determinant = None
    inverse_matrix = None

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.shape = rows, cols
        self.matrix = self.zeros_matrix(rows, cols)

    def zeros_matrix(self, rows, cols):
        return [[0 for _ in range(cols)] for _ in range(rows)]

    def fill_matrix(self):
        print("Enter matrix values: ")
        for i in range(self.rows):
            row = input("> ").split()
            for j in range(self.cols):
                self.matrix[i][j] = float(row[j])
    
    def display(self, det=False):
        print("The result is: ")
        if det and type(self.determinant) == float:
            print(self.determinant)
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    print(self.matrix[i][j], end=" ")
                print()

    def show_determinant(self):
        if type(self.determinant) == float:
            print("The result is: \n", self.determinant)
        else:
            self.display()

    def add_matrix(self, matrix):
        if self.shape != matrix.shape:
            print("The operation cannot be performed.")
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += matrix.matrix[i][j]
            return self.matrix

    def multipy_by_constant(self, constant):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] *= constant
        return self.matrix
    
    def multiply_by_matrix(self, matrix):
        if (self.cols != matrix.rows):
            print("The operation cannot be performed.")
        else:
            product = self.zeros_matrix(self.rows, matrix.cols)
            for i in range(self.rows):
                for j in range(matrix.cols):
                    for k in range(matrix.rows):
                        product[i][j] += self.matrix[i][k] * matrix.matrix[k][j]
            
            self.cols = matrix.cols
            self.shape = self.rows, matrix.cols
            self.matrix = product
            del product
            return self.matrix
    
    def transpose_main_diagonal(self):
        tmp_matrix = self.zeros_matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                tmp_matrix[j][i] = self.matrix[i][j]
        self.matrix = tmp_matrix
        del tmp_matrix
        return self.matrix

    def transpose_side_diagonal(self):
        tmp_matrix = self.zeros_matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                tmp_matrix[i][j] = self.matrix[self.cols - 1 - j][self.rows - 1 - i]
        self.matrix = tmp_matrix
        del tmp_matrix
        return self.matrix

    def transpose_vertical_line(self):
        tmp_matrix = self.zeros_matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                tmp_matrix[i][j] = self.matrix[i][self.cols - 1 - j]
        
        self.matrix = tmp_matrix
        del tmp_matrix
        return self.matrix

    def transpose_horizontal_line(self):
        tmp_matrix = self.zeros_matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                tmp_matrix[i][j] = self.matrix[self.rows - 1 - i][j]
        
        self.matrix = tmp_matrix
        del tmp_matrix
        return self.matrix

    def calculate_determinant(self, matrix=None, total=0):
        if matrix == None: matrix = self.matrix
        if len(matrix) == 2 and len(matrix[0]) == 2:
            self.determinant = float(matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1])
            return self.determinant
        elif len(matrix) > 2 and len(matrix[0]) > 2:
            indices = list(range(len(matrix)))
            for fc in indices:
                tmp_matrix = matrix.copy()[1:]
                height = len(tmp_matrix)

                for i in range(height):
                    tmp_matrix[i] = tmp_matrix[i][0:fc] + tmp_matrix[i][fc + 1:]

                sign = (-1) ** (fc % 2)
                sub_det = self.calculate_determinant(tmp_matrix)
                total += sign * matrix[0][fc] * sub_det

            self.determinant = float(total)
            return total
        else:
            self.determinant = self.matrix
    
    def calcualate_inverse_matrix(self, matrix=None):
        if matrix == None:
            matrix = self.matrix
        n = len(matrix)
        matrix_determinant = self.calculate_determinant()
        if n != len(matrix[0]) or matrix_determinant == 0:
            print("Cannot calculate inverse of this martix.\n"+
            "Matrix is not square-matrix or determinant is equal 0.")
            return -1

        if n == 2:
            self.matrix = [[matrix[1][1]/matrix_determinant, -1*matrix[0][1]/matrix_determinant],
                           [-1*matrix[1][0]/matrix_determinant, matrix[0][0]/matrix_determinant]]
            return self.matrix
        
        cofactors = []
        for r in range(n):
            cofactor_row = []
            for c in range(n):
                minor = [row[:c] + row[c+1:] for row in (matrix[:r] + matrix[r+1:])]
                cofactor_row.append(((-1)**(r+c)) * self.calculate_determinant(minor))
            cofactors.append(cofactor_row)

        self.matrix = cofactors
        cofactors = self.transpose_main_diagonal()

        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/matrix_determinant
        
        # TO DO:
        # correct returnin -0.0 values in cofactor array
        
        self.matrix = cofactors
        return cofactors
      