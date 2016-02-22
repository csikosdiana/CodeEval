import math
def euclidean(x1, y1, x2, y2):
	x, y = x2 - x1, y2 - y1
	return x**2 + y**2

import sys
test_cases = open(sys.argv[1], 'r')
data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.replace(",", " ")
	cord = test.split(" ")
	p = len(cord) // 2
	Edges = [[float("inf")]*p for i in xrange(p)]
	#print Edges
	#print test

	for i in range(0, len(cord) - 2, 2):
		for j in range(i+2, len(cord), 2):
			l = euclidean(int(cord[i]), int(cord[i+1]), int(cord[j]), int(cord[j+1]))
			Edges[i//2][j//2] = l
			Edges[j//2][i//2] = l
	#print Edges
	Stack = [0]
	Sum_MST = 0
	k = 0
	while len(Stack) < p:
		Min_edge = float("inf")
		min_idx = p + 1
		for s in Stack:
			m = min(Edges[s])
			if m < Min_edge:
				Min_edge = m
				k = s
				min_idx = Edges[s].index(m)
		Stack.append(min_idx)
		for j in Stack:
			Edges[j][min_idx] = float("inf")
			Edges[min_idx][j] = float("inf")
		Sum_MST += math.sqrt(Min_edge)
	
	print int(math.ceil(Sum_MST))
	
test_cases.close()