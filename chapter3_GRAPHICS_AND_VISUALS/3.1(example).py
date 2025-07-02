from math import sqrt,sin,pi
import matplotlib.pyplot as plt
import numpy as np
from numpy import empty
from pylab import imshow,gray,show

wavelength = 5.0
k = 2*pi/wavelength
xi0 = 1.0
separation = 20.0 #separation of centres in cm
side = 100.0 #side of the square in cm
points = 500 #number of grid points along each side
spacing = side/points #Spacing of the points in cm

#calculate the positions of the centers of the circles

x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

xi = empty([points,points],float)

for i in range (points):
    y = spacing*i
    for j in range (points):
        x = spacing*j
        r1 = sqrt((x-x1)**2+(y-y1)**2)
        r2 = sqrt((x-x2)**2+(y-y2)**2)
        xi[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2)

imshow(xi,origin='lower',extent = [0,side,0,side])
gray()
show()

