data = ["2 0 6 3 1 6 3 1 6 3 1", "3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49", "1 2 3 1 2 3 1 2 3"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(" ")
	#print nums
	Cycle = ""
	l = 1
	while l < len(nums):
		i = l
		j = 0
		while j < len(nums):
			if nums[j:i] == nums[(j+l):(i+l)]:
				Cycle = " ".join(nums[j:i])
				break
			j = j + 1
			i = i + 1
		l = l + 1
		if Cycle != "":
			print Cycle
			break


#test_cases.close()
