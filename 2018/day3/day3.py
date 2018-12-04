f = open('input.txt', 'r')

from collections import defaultdict


d = defaultdict(int)

def check_dist(d, x, y, width, height):
	for dx in range(1, width+1):
		for dy in range(1, height + 1):
			if d[x + dx, y + dy] > 1:
				return False
	return True


ids = []
locs = []
size = []
for line in f:
	l = line.split()
	for idx in range(len(l)):
		if idx ==0:
			ids.append(int(l[idx][1:]))
		elif idx == 2:
			x, y = l[idx].split(',')
			locs.append([int(x),int(y[:-1])])
		elif idx ==3:
			dx, dy = l[idx].split('x')
			size.append([int(dx), int(dy)])

for idx in range(len(ids)):
	x, y = locs[idx]
	width, height = size[idx]

	for dx in range(1, width+1):
		for dy in range(1, height + 1):
			d[x + dx, y + dy] += 1

overlap = 0
for key in d.keys():
	if d[key] > 1:
		overlap += 1

print('part 1: ', overlap)

for idx in range(len(ids)):
	x, y = locs[idx]
	width, height = size[idx]
	if check_dist(d, x, y, width, height):
		print('part 2: ', ids[idx])


