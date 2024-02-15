from random import uniform


def processing_y(x0, mat, numb):
    y1 = [None] * numb
    for i in range(numb):
        s = 0
        for j in range(numb):
            s += mat[i][j] * x0[j]
        y1[i] = s
    return y1


def processing_x(y1, numb):
    x1 = [None] * numb
    for i in range(numb):
        x1[i] = y1[i] / max(y1)
    return x1


def root_find(y1, x0, numb):
    lambda1 = [0] * numb
    for i in range(numb):
        if abs(x0[i]) > 1e-4:
            lambda1[i] = y1[i] / x0[i]
        else:
            lambda1[i] = None
    return lambda1


with open('input.txt', 'r') as inp:
    n = int(inp.readline().strip())
    eps = 1e-4
    matrix = []
    m_copy = []
    for _ in range(n):
        temp = [float(k) for k in inp.readline().split()]
        matrix.append(temp)
        m_copy.append(temp.copy)

    y_0 = [uniform(-5.0 - i * 0.2, 5.0 + i * 0.3) for i in range(n)]
    x_0 = [y_0[i] / max(y_0) for i in range(n)]

    root0 = [0] * n
    root1 = [0] * n
    ans, vek, flag = 0, 0, 0
    while True:
        y_1 = processing_y(x_0, matrix, n)
        x_1 = processing_x(y_1, n)
        root1 = root_find(y_1, x_0, n)
        print(root1)

        for k in range(n):
            if abs(root1[k] - root0[k]) < eps:
                s = 0
                l = n
                for p in range(n):
                    if root1[p] is None:
                        l -= 1
                        continue
                    s += abs(root1[p])
                ans = s // l
                vek = x_1
                flag = True
                break
        if flag:
            break
        root0 = root1
        x_0 = x_1
        y_0 = y_1
    print(ans, vek)
