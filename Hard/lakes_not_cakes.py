data = ["o # o | # # # | o # o",
		"o # o | # o # | o # o",
		"o o o o # # | o # # # o # | o # # # # # | o o # o o # | # # o # o o | o # # o # o"]

def visited(r, c, max_r, max_c):
	global P
	P[r][c] = "*"
	if r > 0:
		for i in range(-1, 2):
			if c + i >= 0 and c + i <= max_c:
				if P[r-1][c+i] == "o":
					visited(r-1, c+i, max_r, max_c)
	
	for i in [-1, 1]:
		if c + i >= 0 and c + i <= max_c:
			if P[r][c+i] == "o":
				visited(r, c+i, max_r, max_c)
	
	if r < max_r:
		for i in range(-1, 2):
			if c + i >= 0 and c + i <= max_c:
				if P[r+1][c+i] == "o":
					visited(r+1, c+i, max_r, max_c)
			

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
Matrix = []
for test in data:
	test = test.rstrip()
	if len(test) == 0:
		continue
	test = test.split(" | ")
	P = []
	c = 0
	for i in range(len(test)):
		p = test[i].split(" ")
		P.append(p)
		if c == 0:
			c = len(p)
	#print P
	r = len(P)
	Counter = 0
	for i in range(r):
		for j in range(c):
			if P[i][j] == "o":
				Counter += 1
				visited(i, j, r-1, c-1)
				
	print Counter
#test_cases.close()