
import re
import numpy as np
import copy
from collections import defaultdict

def timestep(pos, vel, accel):
    vel[:] = vel[:] + accel[:]
    pos[:] = pos[:] + vel[:]
    return pos, vel, accel



f = open('input.txt', 'r')
minimum = 10000
p = {}
v = {}
a = {}
for i, line in enumerate(f):
    #print(line)
    m =re.search('p=<[-]*[0-9]+,[-]*[0-9]+,[-]*[0-9]+>', line)
    pos = m.group(0)[3:-1].split(',')
    pos = [int(el) for el in pos]
    m =re.search('v=<[-]*[0-9]+,[-]*[0-9]+,[-]*[0-9]+>', line)
    vel = m.group(0)[3:-1].split(',')
    vel = [int(el) for el in vel]
    m =re.search('a=<[-]*[0-9]+,[-]*[0-9]+,[-]*[0-9]+>', line)
    accel = m.group(0)[3:-1].split(',')
    accel = [int(el) for el in accel]

    p[i] = np.array(pos)
    v[i] = np.array(vel)
    a[i] = np.array(accel)

    if sum(np.abs(accel)) <= minimum:
        print(accel, i)
        minimum = sum(np.abs(accel))

        
while(True):
    for p_id in p.keys():
        p[p_id], v[p_id], a[p_id] = timestep(p[p_id], v[p_id], a[p_id])
    #print(p[0])

    collision = defaultdict(set)
    for index, pos in p.items():
        t = tuple(pos)
        collision[t].add(index)
    #print(collision)
    for index, items in collision.items():
        if len(items) > 1:
            for item in items:
                del p[item]
                del v[item]
                del a[item]

    print(len(p))
