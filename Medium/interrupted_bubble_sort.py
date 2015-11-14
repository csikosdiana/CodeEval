data = ["36 47 78 28 20 79 87 16 8 45 72 69 81 66 60 8 3 86 90 90 | 1",
		"40 69 52 42 24 16 66 | 2",
		"54 46 0 34 15 48 47 53 25 18 50 5 21 76 62 48 74 1 43 74 78 29 | 6",
		"48 51 5 61 18 | 2",
		"59 68 55 31 73 4 1 25 26 19 60 0 | 2"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	iters = int(test[1])
	nums = map(int, test[0].split(" "))
	i = min(iters, len(nums)-1)
	while i > 0:
		i -= 1
		for j in range(len(nums)-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
	nums = map(str, nums)
	print " ".join(nums)

#test_cases.close()