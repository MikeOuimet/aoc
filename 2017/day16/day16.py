
def spin(s, n):
	return s[-n:] + s[:-n]

def exchange(s, a, b):
	l = list(s)
	l[a], l[b] = l[b], l[a]
	return ''.join(l)

def partner(s, c1, c2):
	a = s.find(c1)
	b = s.find(c2)
	return exchange(s, a, b)

def dance(s, split):
	for k, el in enumerate(split):
		if el[0] == 's':
			s = spin(s, int(el[1:]))
		if el[0] == 'x':
			a,b = el[1:].split('/')
			s = exchange(s, int(a), int(b))
		if el[0] == 'p':
			c1, c2 = el[1:].split('/')
			s = partner(s, c1, c2)
	return s

s = 'abcdefghijklmnop'

num = 1000000000 % 30
num = 1
f = open('input.txt', 'r')
for line in f:
	split = line.split(',')
	print('Number of instructions: ', len(split))
	for i in range(num):
		s = dance(s, split)

print(s)