import time
from numba import jit
start = time.time()

@jit
def part_two():
	data = 301
	point = 0
	zero = 0
	after_zero = None

	val = 50000000
	length = 1
	for i in range(1,val+1):
		loc = (point + data) % length
		if loc < zero:
			zero += 1
		elif loc ==zero:
			after_zero = i
			print(after_zero)
		length +=1
		point = (loc + 1)%length





def part_one():
	data = 301

	s = [0]
	point = 0

	val = 2017
	for i in range(1,val+1):

		loc = (point + data) % len(s)
		if loc == s.index(0):
			print(i)
		#print('point', loc)
		#print('length', len(s))
		if loc+1 == len(s):
			s = s[:loc+1] + [i]
		else:
			s = s[:loc+1]+[i]+ s[loc+1:]

		point = (loc + 1)%len(s)
		#print(s)
	idx = s.index(2017)
	print(s[idx +1])

#part_one()

print('')
part_two()
print(time.time()- start)