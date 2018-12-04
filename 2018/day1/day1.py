f = open('input.txt', 'r')
from collections import defaultdict

freqs = []
for line in f:
	freqs.append(int(line))

d = defaultdict(int)

idx = 0
cumsum = 0
while True:
	freq = freqs[idx % len(freqs)]
	cumsum += freq
	if d[cumsum] > 0:
		print(cumsum)
		d[cumsum] += 1
		break
	d[cumsum] += 1

	idx += 1