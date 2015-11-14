#data = ['23', '496']

import sys
test_cases = open(sys.argv[1], 'r')
data = test_cases.readlines()
for test in data:
	num = list(test)
	S = 0
	for i in num:
		try:
			k = int(i)
			S = S + k
		except:
			S = S + 0
	print S