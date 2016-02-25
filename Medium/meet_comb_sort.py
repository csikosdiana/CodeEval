data = ['3 1 2',
		'5 4 3 2 1',
		'38 33 44 62 43 88 64 82 95 84']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(' ')
	nums = map(int, nums)
	gap = int(len(nums) / 1.25)
	iter = 0
	while gap > 1:
		b = 0
		e = b + gap
		while e < len(nums):
			if nums[b] > nums[e]:
				nums[b], nums[e] = nums[e], nums[b]
			b += 1
			e += 1
		iter += 1
		gap = int(gap / 1.25)
	
	i = 0
	while i < len(nums) - 1:
		if nums[i] > nums[i+1]:
			nums[i], nums[i+1] = nums[i+1], nums[i]
			iter += 1
			break
		i += 1
	
	print iter

#test_cases.close()