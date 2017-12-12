

def get_largest(vec):
    maxval = vec[0]
    maxid = 0
    for idx, val in enumerate(vec):
        if val > maxval:
            maxid = idx
            maxval = val
    return maxid, maxval


f = open(r'C:\Users\310282769\Desktop\aoc\day6\input.txt', 'r')

for line in f:
   vec= line.split()

for i, num in enumerate(vec):
    vec[i] = int(num)

vec_length = len(vec)

d = []
done = False
total = 0
seen = False

d.append(tuple(vec))
while not done:
    total += 1
    maxid, maxval = get_largest(vec)
    count = maxval
    vec[maxid] = 0
    idx = (maxid+1)%vec_length
    while count >0:
        vec[idx] += 1
        count -= 1
        idx = (idx+1)%vec_length
    tupled = tuple(vec)
    if tupled in d and not seen:
        total = 0
        seen = True
        d = []
        d.append(tupled)
    elif tupled in d and seen:
        done = True
    else:
        d.append(tupled)
    #print(tupled)
print(total)
                
    
    
        
    
    




