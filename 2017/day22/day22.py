f = open('input.txt', 'r')
v_x = 12
v_y = 12



#f = open('test.txt', 'r')
#v_x = 1
#v_y = 1


d = 'u'


def checkgrid(grid, v_x, v_y):
	if (v_y, v_x) not in grid.keys():
		grid[(v_y, v_x)] = 0

	return grid[(v_y, v_x)], grid



def rot(d, check):
	turn = {'u' : ['l', 'r'], 'l' : ['d', 'u'], 'd' : ['r', 'l'], 'r' : ['u', 'd']}
	if check == 0:
		return turn[d][0]
	elif check ==1:
		return d
	elif check ==2:
		return turn[d][1]
	else:
		return turn[turn[d][0]][0]

def move(v_x, v_y, d):
	move = {'u' : (0, -1), 'd' : (0, 1), 'l' : (-1, 0), 'r' : (1, 0)}
	v_x += move[d][0]
	v_y += move[d][1]

	return v_x, v_y

def onetimestep(grid, v_x, v_y, d, count):
	check, grid = checkgrid(grid, v_x, v_y)
	#print(check)
	d = rot(d,check)
	grid[(v_y, v_x)] = (check + 1) % 4
	if check ==1:
		count += 1

	v_x, v_y = move(v_x, v_y, d)

	return grid, v_x, v_y, d, count




count = 0
grid = {}
for j, line in enumerate(f):
	for i, el in enumerate(line):
		if el == '#':
			grid[(j,i)] = 2
		else:
			grid[(j,i)] = 0







for i in range(10000000):
	#print(v_x, v_y, d)
	grid, v_x, v_y, d, count = onetimestep(grid, v_x, v_y, d, count)
	if i%100000 ==0:
		print(i)
	#print(v_x, v_y, d)
	#print('')
	#print('')

print(count)