import math
import numpy as np
import matplotlib.pyplot as plt

def Bessel(m,theta,x):
    return np.cos(m*theta - x*np.sin(theta))

def J(m,x, N=1000):

    a = 0
    b = np.pi
    h = (b-a)/N
    theta = np.linspace(a, b, N+1)

    y = Bessel(m,theta,x)

    S = y[0] + y[1] + 4*np.sum(y[1:N:1])+2*np.sum(y[2:N-1:2])
    return S*(1/3) * h / np.pi

x_vals = np.linspace(0, 20, 200)
J0_vals = [J(0, x) for x in x_vals]
J1_vals = [J(1, x) for x in x_vals]
J2_vals = [J(2, x) for x in x_vals]

plt.plot(x_vals, J0_vals, label='J₀(x)')
plt.plot(x_vals, J1_vals, label='J₁(x)')
plt.plot(x_vals, J2_vals, label='J₂(x)')
plt.title("Bessel Functions $J_0$, $J_1$, and $J_2$")
plt.xlabel("x")
plt.ylabel("$J_m(x)$")
plt.legend()
plt.grid(True)
plt.show()

