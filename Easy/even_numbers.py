data = ['701', '4123', '2936']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	num = int(test)
	if num % 2 == 0:
		print 1
	else:
		print 0
	

#test_cases.close()