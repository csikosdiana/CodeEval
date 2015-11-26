data = ["qttiwkajeerhdgpikkeaaabwl",
		"vavprkykiloeizzt",
		"skwajgaaxqpfcxmadpwaraksnkbgcaukbgli",
		"kaja",
		"bjzanjikh"]

def neighbors(M, r, c, dim):
	N = []
	if r > 0:
		N.append((r-1, c))
	if r < dim:
		N.append((r+1, c))
	if c > 0:
		N.append((r, c-1))
	if c < dim:
		N.append((r, c+1))
	return N

def chain(start, M, dim, letters):
	nexts = neighbors(M, start[0], start[1], dim)
	maxchain = []
	for c in nexts:
		s = M[c[0]][c[1]]
		if s not in letters and Visited[c[0]][c[1]] == 0:
			Visited[c[0]][c[1]] = 1
			l = chain(c, M, dim, letters + [s])
			if len(l) > len(maxchain):
				maxchain = l
			Visited[c[0]][c[1]] = 0
	return [M[start[0]][start[1]]] + maxchain

from math import sqrt
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	N = int(sqrt(len(test)))
	Matrix = []
	for i in xrange(N):
		m = test[(i*N):(i*N+N)]
		m = list(m)
		Matrix.append(m)
	#print Matrix
	Visited = [[0]*N for i in range(N)]
	Longest_path = 0
	for i in xrange(N):
		for j in xrange(N):
			letters = [Matrix[i][j]]
			CH = chain((i, j), Matrix, N-1, letters)
			if len(CH) > Longest_path:
				Longest_path = len(CH)
	print Longest_path
	
#test_cases.close()