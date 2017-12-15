import numpy as np
import time


def to_hex(val):
	v = hex(val)[2:]
	if len(v)==1:
		return '0' + str(v)
	else:
		return str(v)

def to_binary(val):
	v = bin(val)[2:]
	if len(v) == 1:
		s = '000' + v
	elif len(v) ==2:
		s = '00' + v
	elif len(v) ==3:
		s = '0' + v
	else:
		s = v

	return s 



def knot_hash(in_ascii, cycles):
	cursor = 0
	skip = 0
	data = [i for i in range(256)]
	for cycle in range(cycles):
		for size in in_ascii:
			cp = []
			for i in range(size):
				cp.append(data[(i+cursor)%256])
			cp.reverse()
			for i in range(size):
				data[(i+cursor)%256] = cp[i]
			cursor += (size + skip)%256
			skip +=1

	count = 0
	tmp = []
	xor = 0
	hex_val = ''
	for i, el in enumerate(data):
		count += 1
		xor = xor^el
		if count ==16:
			count =0
			tmp.append(xor)
			hex_val += to_hex(xor)
			xor = 0

	return hex_val


input = 'wenycdww-'
#input = 'wenycdww-'

d = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

total = 0

arr = np.zeros(shape = (128,128))

for i in range(128):
	count = 0
	s = ''
	new_input = input + str(i)
	to_ascii = []
	for char in new_input:
		to_ascii.append(ord(char))

	to_ascii += [17, 31, 73, 47, 23]

	my_hash = knot_hash(to_ascii, 64)
	#print(my_hash)

	for char in my_hash:
		if char in '0123456789':
			num = int(char)
		else:
			num = d[char]

		total += bin(num).count('1')
		nums = to_binary(num)
		for num in nums:
			arr[i, count] = num
			count +=1

seen = set()
n = 0
def dfs(i, j):
    if ((i, j)) in seen:
        return
    if not arr[i,j]:
        return
    seen.add((i, j))
    if i > 0:
        dfs(i-1, j)
    if j > 0:
        dfs(i, j-1)
    if i < 127:
        dfs(i+1, j)
    if j < 127:
        dfs(i, j+1)

for i in range(128):
    for j in range(128):
        if (i,j) in seen:
            continue
        if not arr[i,j]:
            continue
        n += 1
        dfs(i, j)

print n


