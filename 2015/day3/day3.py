f = open('input.txt', 'r')
from collections import defaultdict

line = f.readline()

def update(d, delta, loc):
	loc = (loc[0] + delta[0], loc[1] + delta[1])
	d[loc] += 1
	return d, loc



loc = (0,0)
loc_r = (0,0)

d = defaultdict(int)

d[loc] += 2

directions = {'<': (-1, 0), '>': (1, 0), '^': (0, 1), 'v': (0, -1)}
switch = 1
for newdir in line:
	try:
		delta = directions[newdir]
	except:
		print('what was that?!?: ', newdir)
		exit()
	if switch:
		d, loc = update(d, delta, loc)
	else:
		d, loc_r = update(d, delta, loc_r)

	switch = (switch+1)%2

	
print(len(d.keys()))