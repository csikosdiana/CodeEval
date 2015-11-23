data = ['6', '153', '351']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	digits = len(test)
	num = list(test)
	A = 0
	for i in num:
		A = A + (int(i))**digits
	if A == int(test):
		print True
	else:
		print False

#test_cases.close()