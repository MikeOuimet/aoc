f = open('input.txt', 'r')
vec = f.read().split(', ')

d = 'N'
x = 0
y = 0
visits = {}
move = {'N': [[[-1, 0], [1, 0]], ['W', 'E']], 'S': [[[1, 0], [-1, 0]], ['E', 'W']], 'E': [[[0, 1], [0, -1]], ['N', 'S']], 'W': [[[0, -1], [0, 1]], ['S', 'N']]}

def hop(x, y, d, visits, move, new_d, hops):
    for i in range(hops):
        x += move[d][0][new_d][0]
        y += move[d][0][new_d][1]
        if (x,y) in visits.keys():
            return x, y, d, visits, True

        else:
            visits[(x,y)] = 1
    d = move[d][1][new_d]
    return x, y, d, visits, False


done = False
for el in vec:
    hops = int(el[1:])
    if el[0] == 'L':
        x, y, d, visits, done = hop(x, y, d, visits, move, 0, hops)
    else:
        x, y, d, visits, done = hop(x, y, d, visits, move, 1, hops)
    if done:
        break

print(abs(x) + abs(y))