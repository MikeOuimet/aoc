import numpy as np
import copy
f = open('input.txt', 'r')


for line in f:
	data = np.array([int(el) for el in line.split(',')])


def execute(dat, noun, verb):
	data = copy.copy(dat)
	data[1] = noun
	data[2] = verb
	done = False
	idx = 0
	while not done:
		switch = data[idx]
		val1 = data[data[idx+1]]
		val2 = data[data[idx+2]]
		loc = data[idx+3]
		if switch==1:
			data[loc] = val1+ val2
			idx += 4
		elif switch == 2:
			data[loc] = val1*val2
			idx += 4
		elif switch == 99:
			done = True
		else:
			print('uh oh')

	return data[0]

goal = 19690720

for i in range(100):
	for j in range(100):
		if execute(data, i, j) == goal:
			print(i, j, 100*i + j)