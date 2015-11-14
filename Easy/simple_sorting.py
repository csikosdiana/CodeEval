data = ['70.920 -38.797 14.354 99.323 90.374 7.581', '-37.507 -3.263 40.079 27.999 65.213 -55.552']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	numbers = test.split(" ")
	numbers = map(float, numbers)
	numbers = sorted(numbers)
	nums = [format(i, '.3f') for i in numbers]
	print " ".join(nums)

#test_cases.close()