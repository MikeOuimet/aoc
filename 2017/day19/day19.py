
f = open('input.txt', 'r')


data = []
for line in f:
	data.append(line)



w = data[0].find('|')
h = 0
d = 'down'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
move_dict = {'down': [0, 1], 'up': [0, -1], 'left': [-1, 0], 'right' : [1,0]}
reverse_move_dict = { (0,1) : 'down', (0,-1) : 'up', (-1,0) : 'left', (1,0) : 'right'}
continue_set = letters+'-|'
turn_dict = {'left': [[0, 1], [0, -1]], 'right': [[0, 1], [0, -1]], 'up': [[-1, 0], [1, 0]], 'down' : [[-1, 0], [1, 0]]}

s = ''

def one_timestep(w, h, d, s, count, done):
	#print(data[h][w])
	move = move_dict[d]
	neww = w + move[0]
	newh = h + move[1]
	square = data[newh][neww]
	if square in continue_set:
		if square in letters:
			s = s + square
		#count +=1
		return neww, newh, d, s, count+1, False
	elif square == '+':
		directions= turn_dict[d]
		print(directions)
		for direction in directions:
			turnw = neww + direction[0]
			turnh = newh + direction[1]
			turn_square = data[turnh][turnw]
			if turn_square != ' ':
				d = reverse_move_dict[tuple(direction)]
				w = turnw
				h = turnh
				if turn_square in letters:
					s = s + turn_square
				return w, h, d, s, count+2, False
		print("I'm stuck turning!!")

	return w, h, d, s, count, True
count = 1
done = False
while(not done):
	w, h, d, s, count, done = one_timestep(w, h, d, s, count, done)

print(s)
print(count)











