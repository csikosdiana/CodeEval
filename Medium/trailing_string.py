data = ["Hello World,World", "Hello CodeEval,CodeEval", "San Francisco,San Jose"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	string = test[0]
	tail = test[1]
	l = len(tail)
	e = len(string)
	if string[(e-l):e] == tail:
		print 1
	else:
		print 0

#test_cases.close()
