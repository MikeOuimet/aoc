from collections import Counter, defaultdict

f = open('input.txt', 'r')

'''
badset = ['ab', 'cd', 'pq', 'xy']
count = 0
for line in f:
    double = False
    bad = False
    repeat_count = 0
    line = line.split('\n')[0]
    c = Counter(line)
    num_vowels = c['a'] + c['e'] + c['i'] + c['o'] +c['u']
    if num_vowels < 3:
        #pass
        continue
    for idx in range(len(line)-1):
        a = line[idx]
        b = line[idx+1]
        if a==b:
            double = True
        if a+b in badset:
            bad = True
    if double and not bad:
        count +=1

print(count)
'''

count = 0
for line in f:
    double = False
    pair = False
    for idx in range(len(line) - 1):
        a = line[idx]
        b = line[idx+1]
        if a+b in line[idx+2:]:
            pair = True
        if idx < len(line)-2:
            c = line[idx+2]
            if a ==c:
                double = True
    #print()
    if double and pair:
        count+=1

print(count)

