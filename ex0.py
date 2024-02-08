from random import uniform


def processing_y(x0, mat, numb):
    y1 = [None] * numb
    for i in range(numb):
        for j in range(numb):
            y1[i] = mat[i][j] * x0[j]

    return y1

def processing_x(y1, x0):
    

def root_find():




with open('input.txt', 'r') as inp:
    n = int(inp.readline().strip())
    eps = 1e-6
    matrix = []
    m_copy = []
    for _ in range(n):
        temp = [float(k) for k in inp.readline().split()]
        matrix.append(temp)
        m_copy.append(temp.copy)

    y_0 = [uniform(-5.0 - i * 0.2, 5.0 + i * 0.3) for i in range(n)]
    x_0 = [y_0[i] / max(y_0) for i in range(n)]

    root0 = 1
    while abs(root1 - root0) >= eps:
        root1 = processing()
