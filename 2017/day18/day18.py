from collections import deque

f = open('input.txt', 'r')




def to_dict(d, var):
	try:
		d[var] = int(var)
	except:
		if var not in d.keys():
			d[var] = 0
	return d


def add(d, var, val):
	d[var] += int(val)
	return d


def set_to(d, var, val):
	d[var] = int(val)
	return d


def mult(d, var, val):
	d[var] *=int(val)
	return d


def mod(d, var, val):
	d[var] = d[var] % int(val)
	return d


def sound(d, var):
	d['last'] = d[var]
	return d


def send(q, val):
	#print(val)
	#print(q)
	q.append(val)
	#print(q)
	return q

def receive(d, var, q):
	if len(q) == 0:
		return True, d, q
	else:
		val = q.popleft()
		d[var] = val
		return False, d, q



def recover(d, var):
	last = d['last']
	if last > 0:
		d[var] = last
		return True, last
	else:
		return False, last


def jump(d, var, val, point):
	if d[var] >0:
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

def one_timestep(d, arr, point, q_in, q_out, lock, count):
	skip = False
	if point < 0 or point > len(arr):
		lock = True
	else:
		#done = False
		data = arr[point]

		act = data[0]
		var = data[1]
		d = to_dict(d, var)

		if act == 'snd':
			count += 1
			val = get_number(d, var)
			q_out = send(q_out, val)
		elif act == 'rcv':
			lock, d, q = receive(d, var, q_in)
		else:
			#try:
			val = get_number(d, data[2])

			if act == 'set':
				d = set_to(d, var, val)
			elif act == 'mul':
				d = mult(d, var, val)
			elif act =='add':
				d = add(d, var, val)
			elif act == 'mod':
				d = mod(d, var, val)
			
			elif act =='jgz':
				skip, point = jump(d, var, val, point)
		
			else:
				print('Unknown command')
		if skip or lock:
			pass
		else:
			point += 1
		return d, point, q_in, q_out, lock, count


arr = []
for line in f:
	split = line.split()
	arr.append(split)

d0 = {}
d0['p'] = 0
q0 = deque([])

d1 = {}
d1['p'] = 1
q1 = deque([])
#d['last'] = None
p0 = 0
p1 = 0
l0 = False
l1 = False
c0 = 0
c1 = 0
while(not (l0 and l1)):
	for i in range(15):
		d1, p1, q0, q1, l1, c1  = one_timestep(d1, arr, p1, q0, q1, l1, c1)
	for i in range(7):
		d0, p0, q1, q0, l0, c0  = one_timestep(d0, arr, p0, q1, q0, l0, c0)
	
	
	#print(len(q0), len(q1))
	#print(p0, p1)
		#print(point)
print(c0 ,c1)
print(l0, l1)
print(q0, q1)
print(p0, p1)