from collections import defaultdict


def update(t, point, s, count):
	if s == 'A':
		if t[point]:
			t[point] = False
			point -= 1
			s = 'F'
			count -= 1
		else:
			t[point] = True
			point += 1
			s = 'B'
			count +=1
	elif s == 'B':
		if not t[point]:
			t[point] = False
			point += 1
			s = 'C'
		else:
			t[point] = False
			point += 1
			s = 'D'
			count -= 1
	elif s == 'C':
		if not t[point]:
			t[point] = True
			point -= 1
			s = 'D'
			count += 1
		else:
			t[point] = True
			point += 1
			s = 'E'
	elif s == 'D':
		if not t[point]:
			t[point] = False
			point -= 1
			s = 'E'
		else:
			t[point] = False
			point -= 1
			s = 'D'
			count -= 1
	elif s == 'E':
		if not t[point]:
			t[point] = False
			point += 1
			s = 'A'
		else:
			t[point] = True
			point += 1
			s = 'C'
	elif s == 'F':
		if not t[point]:
			t[point] = True
			point -= 1
			s = 'A'
			count += 1
		else:
			t[point] = True
			point += 1
			s = 'A'
	return t, point, s, count




t = defaultdict(bool)

s = 'A'
point = 0
count = 0
num = 12794428
for i in range(num):
	t, point, s, count = update(t, point, s, count)
	if i % 100000==0:
		print(i)
print(count)

c = 0
for key in t.keys():
	if t[key]:
		c+=1

print(c)

