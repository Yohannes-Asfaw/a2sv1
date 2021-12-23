import math

sides = input()
sides = sides.split(" ")
n = int(sides[0])
m = int(sides[1])
a = int(sides[2])
row = math.ceil(n / a)
col = math.ceil(m / a)
squarerow = row * a
squarecol = col * a
print(int((squarecol * squarerow) / (a * a)))
