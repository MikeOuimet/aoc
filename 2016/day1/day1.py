f = open('input.txt', 'r')
vec = f.read().split(', ')

d = 'N'
x = 0
y = 0
visits = {}
move = {'N': [[[-1, 0], [1, 0]], ['W', 'E']], 'S': [[[1, 0], [-1, 0]], ['E', 'W']], 'E': [[[0, 1], [0, -1]], ['N', 'S']], 'W': [[[0, -1], [0, 1]], ['S', 'N']]}
for el in vec:
    hops = int(el[1:])
    for hop in range(hops):
        if el[0] == 'L':
            x += move[d][0][0][0]
            y += move[d][0][0][1]
        else:
            x += move[d][0][1][0]
            y += move[d][0][1][1]
        if (x,y) in visits.keys():
            print(abs(x) + abs(y))
            break
        else:
            visits[(x,y)] = 1
    
    if el[0] == 'L':
        d = move[d][1][0]
    else:
        d = move[d][1][1]

print(abs(x) + abs(y))