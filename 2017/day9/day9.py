import copy
f = open('input.txt', 'r')

for line in f:
	o = copy.copy(line)

skip = False
in_garbage = False
garbage_count = 0

depth = 0
tmp = 0
for i, char in enumerate(o):
	if skip:
		skip = False
	else:
		if char == '!':
			skip = True

		else:
			if in_garbage:
				if char == '>':
					in_garbage = False
				else:
					garbage_count += 1
			else:
				if char == '<':
					in_garbage=True
				else:
					if char == '{':
						depth += 1
					elif char == '}':
						tmp += depth
						depth -=1
			
print(tmp)

print(garbage_count)

