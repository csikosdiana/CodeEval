data = ['3 3 9 1 6 5 8 1 5 3', '9 2 9 9 1 8 8 8 2 1 1', '9 1 7 5 5 6 8 2 5 3 8 7 4 8 7 9 6 3 6', '7 5 3 1 3 3 6 2 7 9 7 2 1 3 6 8 4']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	numbers = test.split(" ")
	nums = dict()
	for i in numbers:
		if i not in nums:
			nums[i] = 1
		else:
			nums[i] += 1
	if 1 not in nums.values():
		print 0
	else:
		unique = []
		for k, v in nums.items():
			if v == 1:
				unique.append(int(k))
		Mini = min(unique)
		winner = numbers.index(str(Mini)) + 1
		print winner

#test_cases.close()