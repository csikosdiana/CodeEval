data = ['3 5 10', '2 7 15']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(" ")
	nums = map(int, nums)
	FB = [0]*nums[2]
	for i in range(1, nums[2] + 1):
		if ((i % nums[0] == 0) and (i % nums[1] == 0)):
			FB[i-1] = 'FB'
		elif (i % nums[0] == 0):
			FB[i-1] = 'F'
		elif (i % nums[1] == 0):
			FB[i-1] = 'B'
		else:
			FB[i-1] = str(i)
	print " ".join(FB)

#test_cases.close()