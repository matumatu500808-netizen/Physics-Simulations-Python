import math
speed = 100
#m/s
g = 9.8
#m/s^2
theta = 30
#degrees
time = speed * math.sin(math.radians(theta)) / g
distance = speed * math.cos(math.radians(theta)) * time
print(distance)