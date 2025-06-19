'''Exercise 2.2: Altitude of a satellite
A satellite is to be launched into a circular orbit around the Earth so that it orbits the
planet once every T seconds.
a) Show that the altitude h above the Earth's surface that the satellite must have is
(
GMT2) t/3
h = 47(2 - R,
where G = 6.67 x 10-11 m3 kg-1 s-2 is Newton's gravitational constant, M
5.97 x 1024 kg is the mass of the Earth, and R = 6371 km is its radius.
b) Write a program that asks the user to enter the desired value of T and then calculates
and prints out the correct altitude in meters.
c) Use your program to calculate the altitudes of satellites that orbit the Earth once
a day (so-called "geosynchronous" orbit), once every 90 minutes, and once every
45 minutes. What do you conclude from the last of these calculations?
d) Technically a geosynchronous satellite is one that orbits the Earth once per sidereal
day, which is 23.93 hours, not 24 hours. Why is this? And how much difference
will it make to the altitude of the satellite?'''

import numpy as np
gravitational_constant = 6.67e-11
mass_of_earth = 5.97e24
R = 6371e3
time = float(input("Write the period of the satellite's orbit in seconds: "))

h = ((gravitational_constant * mass_of_earth*time**2) / (4*np.pi**2))**(1/3) - R

print(h)