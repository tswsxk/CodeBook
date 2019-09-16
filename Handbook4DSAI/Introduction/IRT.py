# coding: utf-8
# 2019/9/16 @ tongshiwei

import functools
import numpy as np
import matplotlib.pyplot as plt
import math

D = 1.7


def irt(a, b, c, theta):
    """
    ..math:
        P(\theta) = c + \frac{(1-c)}{1 + e^{(-Da(\theta-b))}}
    """
    return c + (1 - c) / (1 + math.exp(-D * a * (theta - b)))


def plot_irt():
    a = 2
    b = 0.5
    c = 0.1
    X = np.arange(-3, 3, 0.1)
    irt_f = functools.partial(irt, a, b, c)
    Y = [irt_f(x) for x in X]

    plt.plot(X, Y)
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'Probability of correct response')
    plt.show()


if __name__ == '__main__':
    plot_irt()
