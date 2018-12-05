f = open('input.txt', 'r')

line = f.readline()


def check_alchemy(c1, c2):
	if ((c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper())) and (c1.lower() == c2.lower()):
		return True
	return False

	# test cases
	# print(check_alchemy('c', 'c'))
	# print(check_alchemy('c', 'C'))
	# print(check_alchemy('C', 'C'))
	# print(check_alchemy('C', 'c'))
	# print(check_alchemy('c', 'M'))

def fully_react(s):
	pt = 0
	while True:
		try:
			c1 = s[pt]
			c2 = s[pt+1]
		except:
			break

		if check_alchemy(c1, c2):
			s = s[:pt] + s[pt+2:]
			pt -= 1
		else:
			pt += 1
	return s

def remove_letter(s, letter):
	pt = 0
	while True:
		try:
			c1 = s[pt]
		except:
			break
		if (c1==letter.upper()) or (c1 ==letter.lower()):
			s = s[:pt] + s[pt+1:]
		else:
			pt +=1
	return s
	#testcase
	#print(remove_letter('abcdeABCDEaaaaa', 'a'))


new_s = fully_react(line)

print('part 1: ', len(new_s))

lenred = 50000
for letter in 'abcdefghijklmnopqrstuvwxyz':
	new_s = remove_letter(line, letter)
	reduced_s = fully_react(new_s)
	if len(reduced_s) < lenred:
		lenred = len(reduced_s)

print('part 2: ', lenred)