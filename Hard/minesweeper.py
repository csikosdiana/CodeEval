data = ["3,5;**.........*...",
		"4,4;*........*......"]

		
def neighbour_count(G, r, c):
	global R, C
	Count = 0
	#previous row
	if r - 1 >= 0:
		r1 = r - 1
		for n in range(-1, 2):
			if ((c+n >= 0) and (c+n < C)):
				s = G[r1][c+n]
				if s == "*":
					Count += 1
	
	#current row:
	for n in [-1, 1]:
		if ((c+n >= 0) and (c+n < C)):
			s = G[r][c+n]
			if s == "*":
				Count += 1
	
	#next row
	if r < R - 1:
		r2 = r + 1
		for n in range(-1, 2):
			if ((c+n >= 0) and (c+n < C)):
				s = G[r2][c+n]
				if s == "*":
					Count += 1
	return Count

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	Grid = []
	r = int(test[0].split(",")[0])
	c = int(test[0].split(",")[1])
	R = r
	C = c
	g = []
	for i in test[1]:
		g.append(i)
		if len(g) == c:
			Grid.append(g)
			g = []
	#print Grid
	Result = ""
	for i in range(r):
		for j in range(c):
			if Grid[i][j] == "*":
				Result += "*"
			else:
				Result += str(neighbour_count(Grid, i, j))
	print Result

#test_cases.close()