data = ["2,3,1,0,-4,-1",
		"0,-1,3,-2"]

import itertools
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = map(int, test.split(","))
	zero_count = 0
	C = list(itertools.combinations(nums,4))
	for c in C:
		c = list(c)
		if sum(c) == 0:
			zero_count += 1
	print zero_count
	

#test_cases.close()