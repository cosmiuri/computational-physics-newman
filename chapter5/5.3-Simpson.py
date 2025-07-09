import numpy as np
import matplotlib.pyplot as plt
from math import exp


def f(t):
    return exp(-t**2)


def simpsons_rule(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("Number of slices N must be even for Simpson's Rule.")

    h = (b - a) / N
    s = f(a) + f(b)

    for i in range(1, N, 2):
        s += 4 * f(a + i * h)
    for i in range(2, N, 2):
        s += 2 * f(a + i * h)

    return (h / 3) * s


values_of_x = np.arange(0, 3, 0.001)
values_of_Ex = np.zeros_like(values_of_x)


for i, bound_b in enumerate(values_of_x):
    values_of_Ex[i] = simpsons_rule(f, 0, bound_b, 100)


plt.plot(values_of_x, values_of_Ex, label=r"$\int_0^x e^{-t^2}dt$")
plt.title("Numerical Integration of $e^{-t^2}$ using Simpson's Rule")
plt.xlabel("x")
plt.ylabel("Integral from 0 to x")
plt.grid(True)
plt.legend()
plt.show()
