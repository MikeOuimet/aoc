input_vec = '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118'
in_ascii = []
to_append = [17, 31, 73, 47, 23]
for char in input_vec:
	in_ascii.append(ord(char))
for el in to_append:
	in_ascii.append(el)

print(in_ascii)

def to_hex(val):
	v = hex(val)[2:]
	if len(v)==1:
		return '0' + str(v)
	else:
		return str(v)



#input_vec = [106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118]
cursor = 0
skip = 0


data = [i for i in range(256)]

for cycle in range(64):
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
print(tmp)
print(hex_val)
#print(data[0]*data[1])

