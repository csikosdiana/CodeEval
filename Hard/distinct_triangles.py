data = ["4 5;0 2,0 1,1 2,1 3,2 3",
		"9 3;1 3,1 8,3 8",
		"9 3;5 6,5 7,6 7"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	g = map(int, test[0].split(" "))
	V = g[0]
	E = g[1]
	edges1 = test[1].split(",")
	edges = []
	for e in edges1:
		e = map(int, e.split(" "))
		edges.append([e[0], e[1]])
	#print V, E
	#print edges
	cycles = []
	for i in xrange(V):
		lst = []
		for e in edges:
			if e[0] == i:
				lst.append(e)
		#print lst
		if len(lst) < 2:
			continue
		elif len(lst) == 2:
			if sorted([lst[0][1], lst[1][1]]) in edges:
				c = sorted([i, lst[0][1], lst[1][1]])
				if c not in cycles:
					cycles.append(c)
		else:
			for j in xrange(0, len(lst)-1):
				for k in xrange(j + 1, len(lst)):
					if sorted([lst[j][1], lst[k][1]]) in edges:
						c = sorted([i, lst[j][1], lst[k][1]])
						if c not in cycles:
							cycles.append(c)
	print len(cycles)

#test_cases.close()