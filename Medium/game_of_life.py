data = [".........*",
		".*.*...*..",
		"..........",
		"..*.*....*",
		".*..*...*.",
		".........*",
		"..........",
		".....*..*.",
		".*....*...",
		".....**..."]
	
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
generation = []
for test in data:
	test = test.rstrip()
	generation.append(test)
#test_cases.close()

N = len(generation)
#print generation

def neighbour_count(G, r, c):
	global N
	C = 0
	#previous row
	if r - 1 >= 0:
		r1 = r - 1
		for n in range(-1, 2):
			if ((c+n >= 0) and (c+n < N)):
				s = G[r1][c+n]
				if s == "*":
					C += 1
	
	#current row:
	for n in [-1, 1]:
		if ((c+n >= 0) and (c+n < N)):
			s = G[r][c+n]
			if s == "*":
				C += 1
	
	#next row
	if r < N - 1:
		r2 = r + 1
		for n in range(-1, 2):
			if ((c+n >= 0) and (c+n < N)):
				s = G[r2][c+n]
				if s == "*":
					C += 1
	return C


for i in range(10):
	new_G = []
	for g in range(N):
		new_g = ""
		for k in range(N):
			nb = neighbour_count(generation, g, k)
			if generation[g][k] == "*":
				if nb < 2:
					new_g += "."
				elif nb == 2:
					new_g += "*"
				elif nb == 3:
					new_g += "*"
				elif nb > 3:
					new_g += "."
			elif generation[g][k] == ".":
				if nb == 3:
					new_g += "*"
				else:
					new_g += "."
		new_G.append(new_g)
	generation = new_G
for g in generation:
	print g
	
