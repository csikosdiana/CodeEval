data = ['40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86 86 86 86 86 86 86 86',
		'73 73 73 73 41 41 41 41 41 41 41 41 41 41',
		'1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2',
		'7']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(" ")
	Result = []
	N = []
	c = 0
	i = 0
	while i < len(nums):
		if N == []:
			N.append(nums[i])
			c += 1
			i += 1
		elif nums[i] in N:
			c += 1
			i += 1
		else:
			Result.append(str(c))
			Result.append(nums[i-1])
			N = []
			c = 0
		
		if i == len(nums):
			Result.append(str(c))
			Result.append(nums[i-1])
		
	print " ".join(Result)
	
#test_cases.close()