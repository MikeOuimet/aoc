import numpy as np
f = open('input.txt', 'r')

data = []
for line in f:
	l = line.strip()
	data.append(int(l))

data = np.array(data)
print(data)

def fuel_req(weight):

	weight = weight/3
	weight = np.floor(weight)
	weight = weight - 2
	if weight >0:
		return weight + fuel_req(weight)
	else:
		return 0


fuels = [fuel_req(weight) for weight in data]

print(np.sum(fuels))