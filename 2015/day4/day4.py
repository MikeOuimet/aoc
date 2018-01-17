import hashlib

the_input = 'ckczppom'
test = 'abcdef609043'.encode('UTF-8')
print(hashlib.md5(test).hexdigest())

count = 1
done = False
numzeros = 6

while not done:
	test = 'ckczppom' + str(count)
	myhash = hashlib.md5(test.encode('UTF-8')).hexdigest()[:numzeros]
	if myhash == '0'*numzeros:
		done = True
	else:
		count += 1

print(count, hashlib.md5(test.encode('UTF-8')).hexdigest())




