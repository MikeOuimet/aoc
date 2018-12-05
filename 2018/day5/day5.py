import time
f = open('input.txt', 'r')

line = f.readline()


def fully_react(s):
	stack = []
	for letter in s:
		popped = False
		if stack:
			back = stack[-1]
			if ((letter.isupper() and back.islower()) or (letter.islower() and back.isupper())) and (letter.lower() == back.lower()): 
				stack.pop()
				popped = True
		if not popped:
			stack.append(letter)
	return stack




new_s = fully_react(line)

print('part 1: ', len(new_s))

line = ''.join(new_s)
s = time.time()
lenred = 50000
for letter in 'abcdefghijklmnopqrstuvwxyz':
	new_s = line.replace(letter, '')
	new_s = new_s.replace(letter.upper(), '')
	reduced_s = fully_react(new_s)
	lenred  = min(lenred, len(reduced_s))

print('part 2: ', lenred)
print('Time', time.time() - s)
