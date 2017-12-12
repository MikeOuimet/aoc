
import numpy as np

def word_hashing(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    vec = np.zeros(shape = (1,26))
    for idx, letter in enumerate(letters):
        vec[0, idx] = word.count(letter)
    
    return tuple(vec[0,:])





f = open(r'C:\Users\310282769\Desktop\aoc\day4\input.txt', 'r')


count = 0

for line in f:
   valid = True
   words= line.split()
   d = []
   for word in words:
       letter_hash = word_hashing(word)
       if letter_hash in d:
           valid = False
           break
       else:
           d.append(letter_hash)
   if valid:
       count += 1
print(count)