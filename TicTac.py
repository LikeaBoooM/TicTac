import sys
from random import randint
poleGry = [0,0,0,
	       0,0,0,
	       0,0,0]

wygrane = ([0, 4, 8], [2, 4, 6], [1, 4, 7], [3, 4, 5],
	  [6, 7, 8], [0, 1, 2], [0, 3, 6], [2, 5, 8])
print()
print()
print("        [0][1][2]")
print("        [3][4][5]")
print("        [6][7][8]")
print()
print()
print("Wyżej znajduję się tarcza, która obrazuje pola !")
print("Start | Zaczyna użytkownik !")
print()
while True:
	i = int(input())
	if i <= 8:
		poleGry[i] = 1
	c = 0
	skip1 = 0
	skip = 0

	for x in wygrane:
		if poleGry[x[0]] == 1 and poleGry[x[1]] == 1 and poleGry[x[2]] == 0:
			poleGry[x[2]] = 2
			skip = 1
			break
		elif poleGry[x[0]] == 1 and poleGry[x[1]] == 0 and poleGry[x[2]] == 1:
			poleGry[x[1]] = 2
			skip = 1
			break
		elif poleGry[x[0]] == 0 and poleGry[x[1]] == 1 and poleGry[x[2]] == 1:
			poleGry[x[0]] = 2
			skip = 1
			break
	if skip != 1:
		skip = 0
		for x in wygrane:
			for y in x:
				if y == i and i < x[1]:
					if poleGry[x[1]] == 0:
						poleGry[x[1]] = 2
						skip1 = 1
						break
					elif poleGry[x[2]] == 0:
						poleGry[x[2]] = 2
						skip1 = 1
						break
					else:
						break
				elif y == i and i > x[1]:
					if poleGry[x[1]] == 0:
						poleGry[x[1]] = 2
						skip1 = 1
						break
					elif poleGry[x[2]] == 0:
						poleGry[x[2]] = 2
						skip1 = 1
						break
					else:
						break
				elif y == i and i == x[1]:
					while c == 4 and poleGry[c] != 0:
						c = randint(0, 8)
					poleGry[c] = 2
					break
			if skip1 == 1:
				skip1 = 0
				break
	rysuj = 0
	for x in poleGry:
		print(x, end='  ')
		rysuj = rysuj + 1
		if rysuj == 3:
			rysuj = 0
			print()
