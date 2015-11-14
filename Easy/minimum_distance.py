data = ['4 3 3 5 7', '3 20 30 40']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(" ")
	nums = map(int, nums)
	House = int(sum(nums[1:]) / nums[0])
	Mini_dist = 0
	for i in nums[1:]:
		Mini_dist = Mini_dist + abs(House - i)
	
	k = House
	while True:
		k += 1
		dist = 0
		for i in nums[1:]:
			dist = dist + abs(k - i)
		if dist < Mini_dist:
			Mini_dist = dist
			House = k
		else:
			break
	
	k = House
	while True:
		k -= 1
		dist = 0
		for i in nums[1:]:
			dist = dist + abs(k - i)
		if dist < Mini_dist:
			Mini_dist = dist
			House = k
		else:
			break
	
	print Mini_dist
	
#test_cases.close()

