import numpy as np
#from collections import defaultdict
f = open('input.txt', 'r')

d = {}

def my_hash(arr):
	return arr.tobytes()
	#return tuple(arr.flatten())


def add_rotated(d, sketch, enhance):
	d = add_sketch(d, sketch, enhance)
	for i in range(1,4):
		d = add_sketch(d, np.rot90(sketch, i), enhance)
	return d

def add_sketch(d, sketch, enhance):
	if my_hash(sketch) not in d:
		d[my_hash(sketch)] = enhance
	return d


def to_array(my_list):
	arr = np.empty(shape = (len(my_list), len(my_list)), dtype = bool)
	for i, row in enumerate(my_list):
		for j, el in enumerate(row):
			#print(el)
			if el == '#':
				arr[i,j] = 1
			else:
				arr[i,j] = 0
	return arr

def get_params(size):
	if size % 2 ==0:
		pattern_size = 2
		num_patterns = int(size/2)
		new_size = size + num_patterns
	elif size % 3 ==0:
		pattern_size = 3
		num_patterns = int(size/3)
		new_size = size + num_patterns
	
	return int(new_size), pattern_size, num_patterns 

art = np.array([[0, 1, 0],[0, 0, 1],[1, 1, 1]], dtype = bool)


print(art)

for line in f:
	sketch, enhance = line.split(' => ')
	sketch = sketch.split('/')
	enhance = enhance.rstrip().split('/')
	sketch_arr = to_array(sketch)
	enhance_arr = to_array(enhance)

	d = add_rotated(d, sketch_arr, enhance_arr)
	d = add_rotated(d, np.flipud(sketch_arr), enhance_arr)
	d = add_rotated(d, np.fliplr(sketch_arr), enhance_arr)




for step in range(18):
	size = len(art)
	new_size, pattern_size, num_patterns = get_params(size)
	print(new_size, pattern_size, num_patterns)
	new_art = np.empty(shape = (new_size, new_size), dtype = bool)
	for i in range(num_patterns):
		for j in range(num_patterns):
			block = art[(i)*pattern_size:(i+1)*pattern_size,j*pattern_size:(j+1)*pattern_size]
			new_block = d[my_hash(block)]
			new_art[(i)*(pattern_size+1):(i+1)*(pattern_size+1),j*(pattern_size+1):(j+1)*(pattern_size+1)] = new_block
	art = new_art

print(np.sum(np.sum(new_art)))

'''
0: 3x3
1: 4x4
2: 6x6
3: 9x9
4: 12x12
5: 18x18
'''