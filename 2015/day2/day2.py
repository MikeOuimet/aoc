f = open('input.txt', 'r')

sumval = 0
sumribbon = 0
for line in f:
	nums = line.rstrip().split('x')
	minval = int(nums[0])*int(nums[1])
	for i in range(3):
		val = int(nums[i]) * int(nums[(i+1)%3])
		minval = min(val, minval)
		sumval += 2*val
	sumval += minval

	a = int(nums[0])
	b = int(nums[1])
	if a>b:
		a,b = b,a
	c = int(nums[2])
	if b > c:
		b, c = c,b
	sumribbon += 2*a + 2*b + a*b*c


print(sumribbon)

print(sumval)