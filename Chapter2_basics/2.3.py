"""Exercise 2.3: Write a program to perform the inverse operation to that of Example 2.2.
That is, ask the user for the Cartesian coordinates x, y of a point in two-dimensional
space, and calculate and print the corresponding polar coordinates, with the angle 9
given in degrees."""

from math import sin, cos, pi, asin, acos, sqrt, atan

x = float(input('Enter x:'))
y = float(input('Enter y:'))


r = sqrt(x**2 + y**2)
theta = (atan(y/x)*180)/pi

print(r,theta)
