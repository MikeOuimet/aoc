'''
f = open('input.txt', 'r')
temp = 0
for line in f:
	new = line.split()
	low = int(new[0])
	high = int(new[0])
	for val in new:
		if int(val) < low:
			low = int(val)
		if int(val) > high:
			high = int(val)
	temp += (high - low)

print(temp)
'''

f = open('input.txt', 'r')
temp = 0
for line in f:
	new = line.split()
	for idx, val in enumerate(new):
		for id2 in range(idx+1, len(new)):
			v1 = int(new[idx])
			v2 = int(new[id2])
			if v1 > v2 and v1 % v2 ==0:
				temp += v1/v2
			elif v2 > v1 and v2 % v1 ==0:
				temp += v2/v1

print(temp)

