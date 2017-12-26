from collections import defaultdict
f = open('input.txt', 'r')

def get_other(plug, num):
	if plug[0] == num:
		return plug[1]
	return plug[0]

def get_sum(plug):
	return plug[0] + plug[1]

plug_dict = defaultdict(set)

data = []
for i, line in enumerate(f):
	a,b = line.split('/')
	vals = [int(a), int(b)]
	data.append(vals)

	plug_dict[int(a)].add(i)
	plug_dict[int(b)].add(i)


print(plug_dict[0])

queue = []
ends = []
strengths = []
for item in data:
	if 0 in item:
		queue.append([item])
		ends.append(get_other(item, 0))
		strengths.append(get_sum(item))

#print(queue)
#print(ends)
#print(strengths)

max_s = 0
longest = 1
while queue:
#for i in range(50):
	test = queue.pop()
	end_val = ends.pop()
	strength = strengths.pop()

	#print(test)

	for el in plug_dict[end_val]:
		#print(data[el])
		if len(queue)==1 or 0 not in data[el]:
			if data[el] not in test:
				blah = data[el]
				new_queue = test + [blah]
				#print(new_queue)
				#print(test.append(data[el]))
				queue.append(new_queue)
				ends.append(get_other(data[el], end_val))
				new_s = strength + get_sum(data[el])
				strengths.append(new_s)
				if len(new_queue) > longest:
					longest = len(new_queue)
					print(longest, new_s)
					max_s = new_s
					best = new_queue
				elif len(new_queue) == longest and new_s > max_s:
					print(longest, new_s)
					max_s = new_s
					best = new_queue

print(best)


