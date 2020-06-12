def get_matrix():
    rows, cols = input().split(" ")
    rows, cols = int(rows), int(cols)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        row = input().split(" ")
        for j in range(cols):
            matrix[i][j] = int(row[j])

    return matrix


def multiply_by_scalar(matrix, scalar):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= scalar
    print_matrix(matrix)


def print_matrix(matrix):
    dims = len(matrix), len(matrix[0])
    for i in range(dims[0]):
        row = map(lambda x: str(x), matrix[i])
        print(" ".join(row))


def main():
    matrix_a = get_matrix()
    scalar = int(input())
    multiply_by_scalar(matrix_a, scalar)


if __name__ == "__main__":
    main()



