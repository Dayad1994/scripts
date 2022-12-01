def print_matrix(matrix, n, width=1):
    # вывод матрицы
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def sum_two_matrix(matrix_a, matrix_b, n, m):
    # сложение двух матриц
    matrix_c = []
    for i in range(n):
        str_of_matrix = []
        for j in range(m):
            str_of_matrix.append(matrix_a[i][j] + matrix_b[i][j])
        matrix_c.append(str_of_matrix)
    return matrix_c


def product_two_matrix(matrix_a, matrix_b, n, m, k, l):
    # произведение двух матриц
    matrix_c = []
    for i in range(n):
        str_of_matrix = []
        for j in range(l):
            total = 0
            for p in range(m):
                total += matrix_a[i][p] * matrix_b[p][j]
            str_of_matrix.append(total)
        matrix_c.append(str_of_matrix)
    return matrix_c


def exponentiation_matrix(matrix, n, m):
    # возведение матрицы в степень m
    matrix_c = matrix
    for _ in range(m-1):
        matrix_c = product_two_matrix(matrix_c, matrix, n, n, n, n)
    return matrix_c


# считывание матрицы
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
