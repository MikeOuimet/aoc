f = open('input.txt', 'r')
temp = 0
for line in f:
	new = line.split()
	if len(new)==len(set(new)):
		temp +=1

print temp