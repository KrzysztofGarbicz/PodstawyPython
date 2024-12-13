def multiply_matrices(A, B):

    if len(A[0]) != len(B):
        raise ValueError("Niezogna liczba kolumn")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]


    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [
    [1, 8, 8],
    [1, 3, 6]
]

B = [
    [11, 3],
    [4, 9],
    [0, 1]
]

try:
    result = multiply_matrices(A, B)
    for row in result:
        print(row)
except ValueError as e:
    print(e)
