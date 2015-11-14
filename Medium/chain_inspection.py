data = ["4-2;BEGIN-3;3-4;2-END",
		"4-2;BEGIN-3;3-4;2-3"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.replace("-", " ")
	test = test.replace(";", " ")
	trips = test.split(" ")
	Status = "GOOD"
	T = dict()
	i = 0
	while i < len(trips)-1:
		T[trips[i]] = [trips[i+1], "unvisited"]
		i += 2
	s = "BEGIN"
	while s != "END":
		if T[s][1] == "unvisited":
			T[s][1] = "visited"
			s = T[s][0]
		else:
			Status = "BAD"
			break
	for k, v in T.items():
		if v[1] == "unvisited":
			Status = "BAD"
			break
	print Status

#test_cases.close()