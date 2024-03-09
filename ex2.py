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


def processing(t, t1, y0, temp, func):
    res = [y0]
    t_0 = t
    while t < t1:
        t += temp
        g = sympify(y0 + temp * func - symbols('y')).subs('t', t)
        y0 = newtons_method(t_0, t1, g.subs('t', t))
        res.append(y0)
        print(t, g)
    return res


def temp_mass(t_0, t_1, temp):
    tmp = [t_0]
    while t_0 < t_1:
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

    h = ((T-t0) / 20)
    ans_1 = processing(t0, T, y_0, h, function)
    print(ans_1)
    ans_2 = processing(t0, T, y_0, h/2, function)
    print(ans_2)
    for i in range(len(ans_1)):
        print(f'{round(t0 + i * h, 1)}  |  y1({i}): {round(ans_1[i], 6)}  |  y2({i}): {round(ans_2[i], 6)}')

    tmp1 = temp_mass(t0, T, h)
    tmp2 = temp_mass(t0, T, h/2)
    answ1 = list(map(lambda t: answer.subs('t', t), tmp1))
    answ2 = list(map(lambda t: answer.subs('t', t), tmp2))

    plt.plot(tmp1, ans_1, color='blue')
    plt.plot(tmp2, ans_2, color='orange')
    plt.plot(tmp1, answ1, color='red')
    plt.xlabel('Time')
    plt.ylabel('Values')

    plt.figure()
    plt.text(0, 0.7, 'Function with h step', color='blue')
    plt.text(0, 0.5, 'Function with h/2 step', color='orange')
    plt.text(0, 0.3, 'Correct function', color='red')

    e1 = error_decision(ans_1, answ1)
    e2 = error_decision(ans_2, answ2)

    plt.figure()
    plt.text(0, 0.7, 'Error function with h step', color='red')
    plt.text(0, 0.5, 'Error function with h/2 step', color='blue')
    plt.figure()
    plt.plot(range(0, len(e1)), e1, 'red')
    plt.plot(range(0, len(e1)), e2[:len(e1)], 'blue')
    plt.xlabel('Steps')
    plt.ylabel('Error values')
    plt.show()
#погрешность вывести



