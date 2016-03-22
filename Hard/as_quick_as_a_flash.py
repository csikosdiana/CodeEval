data = ['5 2 6 1 3 4',
		'1 2 3 4',
		'4 3 2 1',
		'3 1 2 4',
		'1 3 2 4',
		'25 21 40 97 6 82 79']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = map(int, test.split(' '))
	swaps = False
	check_pivots = range(len(nums))
	idx = 0
	left = 0
	right = len(nums) - 1
	while True:
		while left < idx:
			if nums[left] > nums[idx]:
				temp = nums[idx]
				nums[idx] = nums[left]
				nums[left] = temp
				idx = left
				left = 0
				right = len(nums) - 1
				swaps = True
				break
			left += 1
		
		while right > idx:
			if nums[right] < nums[idx]:
				temp = nums[idx]
				nums[idx] = nums[right]
				nums[right] = temp
				idx = right
				left = 0
				right = len(nums) - 1
				swaps = True
				break
			right -= 1

		if swaps == True:
			swaps = False
			continue
		else:
			checking = 0
			check_pivots[idx] = "p"
			for i in range(len(nums) - 1):
				try:
					s = sum(check_pivots[i:(i+2)])
					idx = i
					left = i
					right = len(nums) - 1
					swaps = True
					break
				except:
					checking += 1
					if checking == len(nums) - 1:
						swaps = False
					else:
						continue
			if swaps == True:
				swaps = False
				continue
			else:
				break
	
	print check_pivots.count("p")

#test_cases.close()