data = ['thisTHIS', 'AAbbCCDDEE', 'N', 'UkJ']

import string
#print string.ascii_lowercase
#print string.ascii_uppercase

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	whole = 0
	lower = 0
	upper = 0
	for l in test:
		whole += 1
		if l in string.ascii_lowercase:
			lower += 1
		elif l in string.ascii_uppercase:
			upper += 1
	L = (float(lower) / whole) * 100
	U = (float(upper) / whole) * 100
	print("lowercase: %.2f uppercase: %.2f" % (L, U))

#test_cases.close()
