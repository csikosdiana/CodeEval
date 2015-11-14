data = ["4 1 4 2 3", "3 7 7 8", "9 8 9 7 10 6 12 17 24 38"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = map(int, test.split(" "))
	length = nums[0]
	nums = nums[1:]
	#print nums
	diffs = []
	i = 1
	while i < length:
		d = abs(nums[i] - nums[i-1])
		if d not in diffs:
			diffs.append(d)
		i += 1

	if sorted(diffs) == range(1, length):
		print "Jolly"
	else:
		print "Not jolly"

#test_cases.close()
