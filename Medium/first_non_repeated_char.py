data = ['yellow', 'tooth']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	c = 0
	while c < len(test):
		if test[c] not in test[:c] + test[(c+1):]:
			print test[c]
			break
		else:
			c += 1

#test_cases.close()