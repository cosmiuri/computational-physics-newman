"""Exercise 2.4: A spaceship travels from Earth in a straight line at relativistic speed v to
another planet x light years away. Write a program to ask the user for the value of x
and the speed v as a fraction of the speed of light c, then print out the time in years that
the spaceship takes to reach its destination (a) in the rest frame of an observer on Earth
and (b) as perceived by a passenger on board the ship. Use your program to calculate
the answers for a planet 10 light years away with v 0.99c."""

from math import sqrt

c=300000
s = float(input('enter distance: '))
v = float(input('enter speed: '))

t_earth = s/v

t_proper = t_earth*sqrt(1/1-(v/c)**2)

print(t_earth)
print(t_proper)







