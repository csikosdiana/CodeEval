data = ['some line with text', 'another line']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	print test[len(test)-2]

#test_cases.close()