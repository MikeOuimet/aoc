import copy
f = open('input.txt', 'r')

d = {}
#maxval = 0
for line in f:
   statement= line.split()
   vec = copy.copy(statement)
   for i, word in enumerate(statement):
   	if word[-1] == ',':
   		vec[i] = word[:-1]
   #print(vec)

   parent = vec[0]
   children = [el for el in vec[2:] ]

   d[parent] = children


connected = ['0']
to_check = ['0']

while len(to_check)> 0:
	x = to_check.pop()
	newchildren = d[x]
	for child in newchildren:
		if child not in connected:
			connected.append(child)
			if child not in to_check:
				to_check.append(child)


print(len(connected))


