data = ["44 6 1 49 47",
		"34 1 49 2 21",
		"31 38 27 51 18"]

import itertools
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = map(int, test.split(" "))
	P = list(itertools.permutations(nums, 5))
	R = "NO"
	for p in P:
		p = list(p)
		result = [p.pop()]
		while p != []:
			new_result = []
			k = p.pop()
			for i in result:
				x = i + k
				new_result.append(x)
				
				y = i - k
				new_result.append(y)
				
				z = i*k
				new_result.append(z)
			result = new_result
		if 42 in result:
			R = "YES"
			break
	print R

#test_cases.close()

