f = open('input.txt', 'r')
import re
import heapq
import numpy as np
from collections import defaultdict


data_list = []

info = []
h = []
for line in f:
	l = line.strip('\n').split(']')
	date = l[0][1:].split(' ')
	#print(date)

	mo = int(date[0].split('-')[1])
	day = int(date[0].split('-')[2])
	hour = int(date[-1].split(':')[0])
	#if hour ==0:
	#	hour = 24
	minute = int(date[-1].split(':')[-1])

	#key = (mo,day, time)
	payload = l[1][1:]
	if payload[0] == 'G':
		payload = int(re.findall(r'\d+',payload)[0])
	#print(payload)


	entry = (mo, day, hour, minute, payload)
	#print(entry)
	data_list.append(entry)
	info.append(payload)

	heapq.heappush(h, entry)



sleep_dict = defaultdict(lambda: defaultdict(int))

guard = None
asleep = None
while True:
	if guard ==None:
		dataold = heapq.heappop(h) #mo, day, hour, minute, payload
		datanew = heapq.heappop(h)
		if type(dataold[-1])==int: #new guard on duty
			guard = dataold[-1]
			asleep = False
	else:
		try:
			datanew = heapq.heappop(h)
		except:
			break
		if type(dataold[-1])==int: #new guard on duty
			guard = dataold[-1]
			asleep = False
		elif dataold[-1][0] == 'f': # falls asleep
			asleep = True
		elif dataold[-1][0] == 'w': # wakes up
			asleep = False
		else:
			print('uh oh')



	if asleep:
		print(guard)
		minstart = dataold[3]
		totminutes = datanew[3] - dataold[3]
		print('minutes asleep', totminutes)
		for minute in range(totminutes):
			sleep_dict[guard][minute+minstart] +=1
		sleep_dict[guard]['total'] += totminutes

		#print(dataold)
		#print(datanew)




	# print(guard, asleep)
	# print(dataold)
	# print(datanew)
	# print('')

	dataold = datanew


sleepyguard =None
sleeptime = 0
for key in sleep_dict.keys():
	if sleep_dict[key]['total'] > sleeptime:
		sleeptime = sleep_dict[key]['total']
		sleepyguard = key

sleepyday = None
Ndays = 0
for key in sleep_dict[sleepyguard].keys():
	if sleep_dict[sleepyguard][key] > Ndays and (type(key) == int):
		Ndays = sleep_dict[sleepyguard][key]
		sleepyday = key


print('part 1: ', sleepyguard*sleepyday)


g = None
t = None
n= 0
for guardkey in sleep_dict.keys():
	for minkey in sleep_dict[guardkey].keys():
		tp = sleep_dict[guardkey][minkey]
		if tp > n and (type(minkey) == int):
			n = tp
			g = guardkey
			t = minkey

print('part 2: ', g*t)
