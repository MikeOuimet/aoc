
def update_data(data, height, moves, maxside):
    side = maxside
    while side > maxside-moves:
        val = data[height+1, side-1] + data[height+1, side] + data[height+1, side + 1] + data[height, side+1]
        if val > 347991:
            print(val)
            done = True
        else:
            done = False
        data[height, side] = val
        
        side -= 1
    return done, data
    

import numpy as np

size = 51
center = int((size-1)/2)
data = np.zeros(shape = (size, size))
data[center,center] = 1
data[center,center+1] = 1

print(data)
print('')

moves = 2
width_count = 0
height_count = 0
width_move_count = 0
height_once= True


height = center -1
maxside = center  +1

done = False
while not done:
    done, data = update_data(data, height, moves, maxside)
    #print(height, maxside)
    #print(width_count)
    #print(moves)
    width_count += 1
    height_count +=1
    width_move_count +=1
    if width_count >=2:
        moves +=1
        width_count = 0
    if height_count >= 3 and height_once:
        height -= 1
        height_count = 0
        height_once = False
    elif height_count >=4:
        height -= 1
        height_count = 0
    if width_move_count >= 4:
        maxside += 1
        width_move_count = 0
        
    #print(data)
    
    
    #print('')
    
    data = np.rot90(data, k = 3)
    

