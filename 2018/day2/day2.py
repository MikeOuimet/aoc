f = open('input.txt', 'r')

from collections import Counter

def hamming(str1, str2):
	dist = 0
	for idx, c in enumerate(str1):
		if c != str2[idx]:
			dist += 1

	return dist


dubs = 0
trips = 0


data = []
linecount =  0
for line in f:
	d = {}
	#Counter replicator
	for char in line:
		try:
			d[char] += 1
		except KeyError:
			d[char] = 1

	dubflag = True
	tripflag = True
	for key in d.keys():
		if d[key] == 2 and dubflag:
			dubflag = False
			dubs += 1
		elif d[key] ==3 and tripflag:
			tripflag = False
			trips += 1

	data.append(line.strip('\n'))

	linecount += 1


print('part1: ', dubs*trips)


for idx1 in range(linecount):
	for idx2 in range(idx1+1, linecount ):
		l1 = data[idx1]
		l2 = data[idx2]
		h = hamming(l1, l2)
		if h == 1:
			for idx in range(len(l1)):
				if l1[idx] != l2[idx]:
					print('part 2: ', l1[:idx]+ l1[idx+1:])









	#c = Counter(line)
	#print(c)

