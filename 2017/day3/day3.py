import math
import numpy as np
loc = 347991
low = int(math.floor(math.sqrt(loc))**2)
high = int((math.floor(math.sqrt(loc))+2)**2)
sidelen = math.floor(math.sqrt(loc))+2
#print(low)
#print(high)
#print(sidelen)

E = low+(sidelen-1)/2
N = low+3*(sidelen-1)/2
W = low+5*(sidelen-1)/2
S = low+7*(sidelen-1)/2

vec = np.array([E,N, W, S])

dist_to_mid = np.min(np.abs(vec-loc))
dist_to_center = (sidelen-1)/2

print(dist_to_mid)

print(dist_to_center+dist_to_mid)
