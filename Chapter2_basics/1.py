h = float(input("Enter height in meters: "))
t = float(input("Enter time in seconds: "))
g = 9.81
s = g*t**2/2

print('the height of the ball is ', h-s,'meters')