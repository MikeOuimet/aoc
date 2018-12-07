f = open('input.txt', 'r')
import numpy as np
from collections import defaultdict

d = defaultdict(int)

def unique_closest(pt, ptset):
	setsize, blah = np.shape(ptset)
	unique = True
	mindist = 10000000000
	minid = None
	for idx in range(setsize):
		dist = abs(pt[0] - ptset[idx][0]) + abs(pt[1] - ptset[idx][1])
		if dist == mindist:
			unique = False
		elif dist < mindist:
			unique = True
			mindist = dist
			minid = idx

	return unique, minid

def within_bounds(pt, ptset, bound):
	setsize, blah = np.shape(ptset)
	count = 0
	for idx in range(setsize):
		dist = abs(pt[0] - ptset[idx][0]) + abs(pt[1] - ptset[idx][1])
		count += dist
		if count >=bound:
			return False
	return True



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


datalen, blah = np.shape(data)


#part 1
# owners = np.zeros(datalen)
# owners2 = np.zeros(datalen)
# for x in range(xmin-1, xmax+2):
# 	for y in range(ymin-1, ymax + 2):
# 		#print(x,y)
# 		uniqueFlag, closestid = unique_closest([x,y], data)
# 		if uniqueFlag:
# 			owners[closestid] += 1

# for x in range(xmin-2, xmax+3):
# 	for y in range(ymin-2, ymax + 3):
# 		#print(x,y)
# 		uniqueFlag, closestid = unique_closest([x,y], data)
# 		if uniqueFlag:
# 			owners2[closestid] += 1


# maxsame = 0
# for idx in range(datalen):
# 	if owners2[idx] == owners[idx]:
# 		maxsame = max(maxsame, owners[idx])

# print(maxsame)


safecount = 0
for x in range(xmin-1, xmax+2):
	for y in range(ymin-1, ymax + 2):
		#print(x,y)
		if within_bounds([x,y], data, 10000):
			safecount += 1

print(safecount)



		