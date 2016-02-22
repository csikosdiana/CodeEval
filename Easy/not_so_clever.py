data = ['4 3 2 1 | 1',
		'5 4 3 2 1 | 2']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	T = test.split(' | ')
	nums = map(int, T[0].split(' '))
	iter = int(T[1])
	for k in range(iter):
		for i in range(len(nums) - 1):
			if nums[i] > nums[i+1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]
				break
		
	nums = map(str, nums)
	print ' '.join(nums)

#test_cases.close()