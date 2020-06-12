def get_matrix():
    rows, cols = input().split(" ")
    rows, cols = int(rows), int(cols)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        row = input().split(" ")
        for j in range(cols):
            matrix[i][j] = int(row[j])

    return matrix


def add_marices(matrix_a, matrix_b):
    dims_a = len(matrix_a), len(matrix_a[0])
    dims_b = len(matrix_b), len(matrix_b[0])
    if dims_a != dims_b:
        print('ERROR')
    else:
        for i in range(dims_a[0]):
            for j in range(dims_a[1]):
                matrix_b[i][j] += matrix_a[i][j]
        print_matrix(matrix_b)


def print_matrix(matrix):
    dims = len(matrix), len(matrix[0])
    print()
    for i in range(dims[0]):
        row = map(lambda x: str(x), matrix[i])
        print(" ".join(row))


def main():
    matrix_a = get_matrix()
    matrix_b = get_matrix()
    add_marices(matrix_a, matrix_b)


if __name__ == "__main__":
    main()


