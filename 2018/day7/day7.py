f = open('input.txt', 'r')
from collections import defaultdict
import heapq
import numpy as np

dependencies = defaultdict(list)
dependents = defaultdict(list)

sort = []
openlist = []
totallist = []
for line in f:
	l1, l2 = line[5], line[36]  #l2 depends on l1

	dependencies[l2] += l1
	dependents[l1] += l2
	totallist.append(l1)
	totallist.append(l2)

totallist = set(totallist)

for item in totallist:
	if not dependencies[item]:
		heapq.heappush(openlist, item)

print(openlist)

nworkers = 5
busy = [False, False, False, False, False]
task = [None, None, None, None, None]
timeleft = [0, 0, 0, 0, 0]

t = 0
while openlist or any(busy):

	for worker in range(nworkers):
		if not busy[worker]:
			if openlist:
				nextstep = heapq.heappop(openlist)
				task[worker] = nextstep
				print('task assigned', nextstep, ' to worker', worker )
				timeleft[worker] =ord(nextstep) - 64 +60# update to right time
				#print(nextstep, timeleft[worker])

				busy[worker] = True


	t += 1
				
	for worker in range(nworkers):	
		if busy[worker]:
			timeleft[worker] -= 1
			if timeleft[worker] == 0:

				done = task[worker]
				print('time: ',t, 'task completed :', done)
				sort.append(done)
				for deps in dependents[done]:
					#print('deps', deps)
					dependencies[deps].remove(done)
					if not dependencies[deps]:
						heapq.heappush(openlist, deps)		
				busy[worker] = False
				task[worker] = None
				print('open list', openlist)

		# if not busy[worker]:
		# 	if openlist:
		# 		nextstep = heapq.heappop(openlist)
		# 		task[worker] = nextstep
		# 		print('task assigned', nextstep, ' to worker', worker )
		# 		timeleft[worker] =ord(nextstep) - 64 # update to right time
		# 		print(nextstep, timeleft[worker])

		# 		busy[worker] = True
				



strsort = ''
for letter in sort:
	strsort += letter

print(strsort)
print(t)
