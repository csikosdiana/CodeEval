data = ['1 2 2, 1 3 3, 3 4 3, 2 4 6, 4 5 16, 3 5 7 | 1 5',
		'1 2 3, 2 8 10, 1 9 4, 8 9 2 | 2 8',
		'5 9 6, 10 9 15, 10 8 44, 10 7 48, 5 7 5, 10 5 3, 10 4 30, 10 3 38, 4 9 45, 3 9 42, 6 7 50, 7 9 6, 6 9 26, 5 6 14, 3 7 3 | 5 3',
		'10 8 32, 10 7 13, 3 4 30, 10 5 3, 10 3 40, 4 9 44, 3 9 14, 6 7 31, 7 9 50, 6 9 20, 6 8 36, 5 6 16, 3 7 16 | 2 6']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	T = test.split(' | ')
	goal = map(int, T[1].split(' '))
	#print goal
	E = T[0].split(', ')
	edges = {}
	shortest_paths = {}
	for i in E:
		e = map(int, i.split(' '))
		edges[(e[0], e[1])] = e[2]
		edges[(e[1], e[0])] = e[2]
		
		if e[0] not in shortest_paths:
			shortest_paths[e[0]] = float("Inf")
		if e[1] not in shortest_paths:
			shortest_paths[e[1]] = float("Inf")
	if goal[0] not in shortest_paths:
		print False
		continue
	elif goal[1] not in shortest_paths:
		print False
		continue
	else:
		shortest_paths[goal[0]] = 0
	
	#print edges
	V = shortest_paths.keys()
	#print V
	#print shortest_paths
	s = goal[0]
	visited = [s]
	V.remove(s)
	while len(visited) != len(shortest_paths):
		temp1 = []
		temp2 = []
		for i in V:
			if (s, i) in edges:
				if shortest_paths[s] + edges[(s, i)] < shortest_paths[i]:
					shortest_paths[i] = shortest_paths[s] + edges[(s, i)]
			temp1.append(i)
			temp2.append(shortest_paths[i])
		m = min(temp2)
		idx = temp2.index(m)
		s = temp1[idx]
		visited.append(s)
		V.remove(s)
	if shortest_paths[goal[1]] == float("Inf"):
		print False
	else:
		print shortest_paths[goal[1]]

#test_cases.close()