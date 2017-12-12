
f = open('input.txt', 'r')

for line in f:
	data = line.strip('\n')
	data= data.split(',')



def diags(vec):
	# n ne se s sw nw
	for i in range(6):
		tmp = min(vec[i], vec[(i+2)%6])
		vec[(i+1)%6]  += tmp
		vec[i] -= tmp
		vec[(i+2)%6] -= tmp
	return vec

def across(vec):
	# n ne se s sw nw
	for i in range(3):
		tmp = min(vec[i], vec[i+3])
		vec[i] -= tmp
		vec[i+3] -= tmp
	return vec


def update(vec):
	# n ne se s sw nw
	vec = diags(vec)
	vec = across(vec)
	vec = diags(vec)
	vec = across(vec)
	return vec

ivec = [0, 0, 0, 0, 0, 0]
maxd = 0
for el in data:
	if el == 'n':
		ivec[0] += 1
	elif el == 'ne':
		ivec[1] +=1
	elif el == 'se':
		ivec[2] += 1
	elif el == 's':
		ivec[3] += 1
	elif el == 'sw':
		ivec[4] += 1
	else:
		ivec[5] += 1
	ivec = update(ivec)
	dist = sum(ivec)
	if dist > maxd:
		maxd = dist
		#print(dist)
print(maxd)
print(dist)



