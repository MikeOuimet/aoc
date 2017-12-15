# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f = open('C:/Users/ouimet/Desktop/aoc/day13/input.txt', 'r')
locs = []
depths = []
for line in f:
    #print(line)
    
    tmp = line.split(':')
    locs.append(int(tmp[0]))
    depths.append(int(tmp[1]))

#print(locs)
#print(depths)

#locs = [0, 1, 4, 6]
#depths = [3, 2, 4, 4]



blah = 0
safe = False
delay = 10
caught = False
while not safe:
    #print(delay)

    for i, loc in enumerate(locs):
        arrive_at = loc + delay
        if arrive_at % (2*(depths[i]-1) ) ==0:
            caught = True
            blah += depths[i]*loc
   # print(blah)
    if caught:
        blah = 0
        delay += 1
        caught = False
    else:
        safe = True
    #print('')

print(delay)