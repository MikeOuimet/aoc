

f = open('input.txt', 'r')
vec = []
for line in f:
   vec.append(int(line))

problem_length = len(vec)

idx = 0
count = 0
done = False
while not done:
    num_jumps = vec[idx]
    count += 1
    if num_jumps + idx <0 or num_jumps + idx >= problem_length:
        done = True
    else:
        if num_jumps <3:
            vec[idx] += 1
        else:
            vec[idx] -=1
            
        idx += num_jumps

print(count)