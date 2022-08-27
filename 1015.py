import math
from math import sqrt

x = input().split()
x1 = float(x[0])
y1 = float(x[1])

y = input().split()
x2 = float(y[0])
y2 = float(y[1])

dist = sqrt((x2-x1)**2 + (y2-y1)**2)

print(round(dist, 4))
