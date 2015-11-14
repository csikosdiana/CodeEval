data = ['-10,2,3,-2,0,5,-15', '2,3,-2,-1,10']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(",")
	nums = map(int, nums)
	BIG_SUM = nums[0]
	for i in range(0, len(nums)):
		for j in range(i+1, len(nums)+1):
			SUM = sum(nums[i:j])
			if SUM > BIG_SUM:
				BIG_SUM = SUM
	print BIG_SUM
	
#test_cases.close()