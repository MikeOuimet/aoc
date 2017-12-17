cimport cython
cdef long long A = 722
cdef long long B = 354



cdef long long mult_A = 16807
cdef long long mult_B = 48271

cdef long long div = 2147483647

#A =65
#B = 8921

cdef long long big =  2**16


cdef int count = 0
cdef int i
for i in range(5e6):
#for i in range(5):
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


print(count)
