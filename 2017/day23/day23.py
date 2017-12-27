'''
def to_dict(d, var):
	try:
		d[var] = int(var)
	except:
		if var not in d.keys():
			d[var] = 0
	return d


def dec(d, var, val):
	d[var] -= int(val)
	return d


def set_to(d, var, val):
	d[var] = int(val)
	return d


def mult(d, var, val):
	d[var] *=int(val)
	return d


def jump(d, var, val, point):
	if d[var] != 0:
		point += int(val)
		return True, point
	else:
		return False, point


def get_number(d, var):
	if var in d.keys():
		return d[var]
	else:
		try:
			return int(var)
		except:
			print('Not sure what this is')


f = open('input.txt' , 'r')

d = {}
keys = 'abcdefgh'
for el in keys:
	d[el] = 0
d['a'] = 1
d['b'] = 108100
d['c'] = 125100
d['1'] = 1



instructions = []
for line in f:
	act, var, val = line.strip('\n').split(' ')
	instructions.append([act, var, val])




point = 0
count = 0
while point >=0 and point< len(instructions):
	if point == 19:
		print(point)
		print(d['a'], d['b'], d['c'], d['d'],d['e'], d['f'], d['g'], d['h'] )
		print('')
	skip = False
	act,var, val = instructions[point]

	if act == 'set':
		val = get_number(d, val)
		d = set_to(d, var, val)
	elif act == 'sub':
		val = get_number(d, val)
		d = dec(d, var, val)
	elif act == 'mul':
		val = get_number(d, val)
		d = mult(d, var, val)
		count += 1
	elif act == 'jnz':
		skip, point = jump(d, var, val, point)

	if not skip:
		point += 1

	

print(count)


'''
def not_prime(num):
	for val in range(2, int(num**(.5))+1):
		if num % val == 0:
			return True
	return False

val = 108100
end = 125100
add = 17
count = 0
while val <= end:
	if not_prime(val):
		count += 1
	val +=17

print(count)



