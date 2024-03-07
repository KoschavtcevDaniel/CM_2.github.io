from sympy import sympify, symbols, diff, Float
from math import fabs
import matplotlib.pyplot as plt
from time import sleep
eps = 1e-6


def f(per, tmp, var):
    return tmp.subs(var, per)


def newtons_method(a, b, func, var='y'):
    if f(a, func, var) * f(a, diff(func, var, 2), var) > 0:
        x_1 = a
    else:
        x_1 = b
    x_2 = x_1 - f(x_1, func, var) / f(x_1, diff(func, var), var)
    while fabs(x_2 - x_1) > eps and fabs(f(x_2, func, var)) > eps:
        if f(x_2, func, var) < f(x_1, func, var):
            x_1 = x_2
            x_2 = x_1 - f(x_1, func, var) / f(x_1, diff(func, var), var)
        else:
            x_1 = (x_1 + x_2) / 2
            x_2 = x_1 - f(x_1, func, var) / f(x_1, diff(func, var), var)
    res = Float(x_2)
    return res


def processing(t, t1, y0, temp, g, func):
    res = []
    while t < t1:
        t += temp
        res.append(y0)
        y0 = newtons_method(t0, t1, g)
        g = sympify(y0 + temp * func - symbols('y'))
    return res


def temp_mass(t_0, t_1, temp):
    tmp = [t_0]
    while t_0 < t_1 - temp:
        t_0 += temp
        tmp.append(round(t_0, 6))
    return tmp


def error_decision(tmp, dec):
    err = []
    for ind in range(len(tmp)):
        err.append(dec[ind] - tmp[ind])
    return err


with open('inp3.txt', 'r') as file:
    function = sympify(file.readline())
    t0, T = float(file.readline()), float(file.readline())
    y_0 = float(file.readline())
    answer = sympify(file.readline())

    h = (5 * 0.2) / (T-t0)
    g1 = sympify(y_0 + h * function - symbols('y'))
    g2 = sympify(y_0 + h / 2 * function - symbols('y'))
    ans_1 = processing(t0, T, y_0, h, g1, function)
    ans_2 = processing(t0, T, y_0, h/2, g2, function)

    print(ans_1)
    print(ans_2)
    for i in range(len(ans_1)):
        print(f'{round(t0 + i * h, 1)}  |  y1({i}): {round(ans_1[i], 6)}  |  y2({i}): {round(ans_2[i], 6)}')

    tmp1 = temp_mass(t0, T, h)
    tmp2 = temp_mass(t0, T, h/2)
    answ1 = list(map(lambda t: answer.subs('t', t), tmp1))
    answ2 = list(map(lambda t: answer.subs('t', t), tmp2))

    plt.figure()
    plt.plot(tmp1, ans_1, 'blue')
    plt.plot(tmp2, ans_2, 'orange')
    plt.plot(tmp1, answ1, 'red')
    plt.show()

    e1 = error_decision(ans_1, answ1)
    e2 = error_decision(ans_2, answ2)

    plt.figure()
    plt.plot(range(0, len(e1)), e1, 'red')
    plt.plot(range(0, len(e2)), e2, 'blue')
    plt.show()
#погрешность вывести



