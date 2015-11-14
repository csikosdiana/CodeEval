data = ["1,2,3,4,5;2", "1,2,3,4,5;3", "10,11,12,13,14,15,16,17,18,19,20;7"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	groups = int(test[1])
	nums = test[0].split(",")
	i = 0
	while i + (groups - 1) < len(nums):
		N = nums[:i] + nums[i:(i+groups)][::-1] + nums[(i+groups):]
		i += groups
		nums = N
	print ",".join(nums)
	

#test_cases.close()
