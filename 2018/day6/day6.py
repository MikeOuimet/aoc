f = open('input.txt', 'r')
import numpy as np


data = []
for line in f:
	x,y = line.split(',')
	x,y = int(x), int(y)
	data.append([x,y])

data = np.array(data)

xmax, ymax = np.max(data, axis = 0)
xmin, ymin = np.min(data, axis = 0)

width = xmax - xmin + 2
height = ymax - ymin + 2

print(width, height)


for x in range(width):
	for y in range(height):
		