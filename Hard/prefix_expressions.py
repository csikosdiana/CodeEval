data = ["* + 2 3 4",
		"* * * + + * 1 2 5 4 5 9 8",
		"* * * + / * / 3 8 6 4 8 9 0 5"]

import operator
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(" ")
	methods = []
	nums = []
	for i in test:
		try:
			n = int(i)
			nums.append(n)
		except:
			methods.append(i)
	#print methods
	#print nums
	s = nums[0]
	i = 1
	while len(methods) > 0:
		m = methods.pop()
		if m == "*":
			s = operator.mul(s, nums[i])
		elif m == "+":
			s = operator.add(s, nums[i])
		elif m == "/":
			s = operator.truediv(s, nums[i])
		i += 1
	print int(round(s))		

#test_cases.close()