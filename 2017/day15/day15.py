import day15_cy
'''
import time
start = time.time()
A = 722
B = 354



mult_A = 16807
mult_B = 48271

div = 2147483647

#A =65
#B = 8921

big =  2**16


count = 0
tmp =0
size = 50000
for i in range(size):

	A = (A * mult_A) % div
	B = (B * mult_B) % div
	while A %4 != 0:
		A = (A * mult_A) % div
	while B%8 != 0:
		B = (B * mult_B) % div



	if A%big == B%big:
		#print(i)
		count +=1
		

	#bA = bin(A)[2:].rjust(16,'0')
	#bB = bin(B)[2:].rjust(16,'0')


print(time.time() -start)

'''