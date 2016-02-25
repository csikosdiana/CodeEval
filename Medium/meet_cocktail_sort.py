data = ['5 4 9 10 7 3 2 1 6 | 1',
		'9 8 7 6 5 4 3 2 1 | 3']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	T = test.split(' | ')
	nums = map(int, T[0].split(' '))
	iter = int(T[1])
	b = 0
	e = len(nums) - 1
	i = 0
	while i < iter:
		for k in range(b, e):
			if nums[k] > nums[k + 1]:
				nums[k], nums[k+1] = nums[k+1], nums[k]
		e -=1
		
		for h in range(e, b, -1):
			if nums[h] < nums[h-1]:
				nums[h], nums[h-1] = nums[h-1], nums[h]
		
		b += 1
		
		i += 1
	
	nums = map(str, nums)
	print ' '.join(nums)

#test_cases.close()