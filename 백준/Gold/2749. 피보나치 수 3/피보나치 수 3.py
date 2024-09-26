def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 1000000, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 1000000],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 1000000, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 1000000]
    ]

def matrix_pow(M, power):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    base = M

    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2

    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    F = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(F, n - 1)

    return result_matrix[0][0]

n = int(input())
print(fibonacci(n))
