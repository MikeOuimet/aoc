f = open('input.txt', 'r')
for line in f:
	print(line.count('(') - line.count(')'))


	loc =0
	for i, char in enumerate(line):
		if char =='(':
			loc += 1
		else:
			loc -= 1
		if loc <0:
			print(i+1)
			break

