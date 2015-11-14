data = ['abcabcabcabc', 'bcbcbcbcbcbcbcbcbcbcbcbcbcbc', 'dddddddddddddddddddd', 'adcdefg']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	c = 0
	while c < len(test):
		if test[:(c+1)] == test[(c+1): (2*(c+1))]:
			c += 1
			break
		else:
			c += 1
		
	print c

#test_cases.close()