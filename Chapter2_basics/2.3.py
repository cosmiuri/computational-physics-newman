from math import sin, cos, pi, asin, acos, sqrt, atan

x = float(input('Enter x:'))
y = float(input('Enter y:'))


r = sqrt(x**2 + y**2)
theta = (atan(y/x)*180)/pi

print(r,theta)
