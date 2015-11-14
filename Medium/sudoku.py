data = ["4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2",
		"4;2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1"]

import math
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	N = int(test[0])
	nums = test[1].split(",")
	nums = map(int,nums)
	Valid = True
	
	rows = []
	i = 0
	while i < len(nums):
		r = nums[i:(i+N)]
		
		if sorted(r) != range(1, N+1):
			Valid = False
			break

		rows.append(r)
		i = i + N
	if Valid == False:
		print Valid
		continue
		
	cols = []
	i = 0
	while i < N:
		c = []
		for j in range(i, len(nums), N):
			c.append(nums[j])
		
		if sorted(c) != range(1, N+1):
			Valid = False
			break
			
		cols.append(c)
		i += 1

	if Valid == False:
		print Valid
		continue
	
	R = int(math.sqrt(N))
	regions = []
	j = 0
	i = 0
	r = []
	while j < R:
		k = i
		while i < len(nums):
			p = nums[i:(i+R)]
			for h in p:
				r.append(h)
			if len(r) == N:
				if sorted(r) != range(1, N+1):
					Valid = False
					break
		
				regions.append(r)
				r = []
			i = i + N
		i = k + R
		j = j + 1
	if Valid == False:
		print Valid
		continue
	
	print Valid
	

#test_cases.close()