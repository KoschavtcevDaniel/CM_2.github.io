from time import sleep


def copy(matrix, numb):
    ans = []
    for i in range(numb):
        ans.append(matrix[i].copy())
    return ans


def evaluation_matrix(matrix1, matrix0, numb):
    mult = [[None for _ in range(numb)] for _ in range(numb)]
    for i in range(numb):
        for j in range(numb):
            mult[i][j] = sum(matrix1[i][t] * matrix0[t][j] for t in range(numb))
    return mult


def summing(matrix, numb):
    s = 0
    for i in range(numb):
        for j in range(numb):
            if i != j:
                continue
            s += matrix[i][j]
    return s


with open('input2.txt', 'r') as inp:
    n = int(inp.readline().strip())
    k = 2 ** n
    eps = 1e-6
    A = []
    print("Let's go")

    for _ in range(n):
        temp = [float(k) for k in inp.readline().split()]
        A.append(temp)

    # lambda0 = -10000
    step = 0
    A_0 = copy(A, n)
    sleep(2)
    while step < k:
        A_1 = evaluation_matrix(A_0, A, n)
        s1, s0 = summing(A_1, n), summing(A_0, n)
        if s0 == 0:
            lambda1 = 0
        else:
            lambda1 = s1 / s0
        step += 1
        A_0 = A_1
        # if abs(lambda1 - lambda0) < eps:
        #     break

    print('\n', '-'*10 + 'Answer' + 10 * '-', '\n')
    print("Lambda is ", round(lambda1))
    print('\n', '-' * 26)
