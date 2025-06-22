'''Exercise 2.5: Quantum potential step
A well-known quantum mechanics problem involves a particle of mass m that encounters
a one-dimensional potential step, like this:
---------- --------------- E
R T
incoming
0
The particle with initial kinetic energy E and wavevector k1 = ,,/im£/t1 enters from the
left and encounters a sudden jump in potential energy of height V at position x = 0.
By solving the Schrtidinger equation, one can show that when E > V the particle may
either (a) pass the step, in which case it has a lower kinetic energy of E - Von the other
side and a correspondingly smaller wavevector of k2 = J2m(E - V)/t1, or (b) it may
be reflected, keeping all of its kinetic energy and an unchanged wavevector but moving
in the opposite direction. The probabilities T and R for transmission and reflection are
given by
R = (k1 -k2)
2
k1 +k2
Suppose we have a particle with mass equal to the electron mass 111 = 9.11 x
10-31 kg and energy lOeV encountering a potential step of height 9eV. Write a Python
program to compute'''
from math import sqrt

m = 9.11e-31
eV = 1.602e-19
E = 10*eV
V = 9*eV
hbar = 1.05e-34

k1 = sqrt(2*m*E)/hbar
k2 = sqrt(2*m*(E-V))/hbar

T = 4*k1*k2/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print('T = ',T, 'R = ',R)


